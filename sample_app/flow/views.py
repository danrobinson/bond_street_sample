from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Step, UserStep

class StepView(LoginRequiredMixin, View):

    template_name = 'flow/step.html';

    def get_object(self):
        step_number = self.kwargs.get('step_number')
        user_step = get_object_or_404(UserStep.objects.select_related('step'),
                                      step__number=int(step_number),
                                      user=self.request.user)
        return user_step

    def get_context_data(self):
        context = {}
        context['user_step'] = self.object
        context['user_steps'] = UserStep.objects \
                                        .filter(user=self.request.user) \
                                        .select_related('step')
        return context

    def get(self, request, **kwargs):
        self.kwargs = kwargs
        self.object = self.get_object()
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        self.request = request
        self.kwargs = kwargs
        self.object = self.get_object()
        # if the form had any information, we'd validate it here
        # if it were invalid, we'd re-render the page with an error message
        # if it were valid, we'd save the data to the database
        # as it is, we just mark the step as completed
        self.object.completed = True
        self.object.save()
        step = self.object.step
        later_user_steps = UserStep.objects \
                                   .filter(user=request.user, 
                                           step__gt=step.number) \
                                   .order_by("-step__number")
        if later_user_steps.count():
            # the user has later steps in progress
            # redirect them to their 
            return redirect(later_user_steps[0])
        else:
            try:
                # create a UserStep for the next step
                # and redirect to it
                next_step = Step.objects.get(number=step.number + 1)
                next_user_step = UserStep.objects.create(step=next_step, 
                                                         user=request.user)
                return redirect(next_user_step)
            except Step.DoesNotExist:
                # the user has completed all steps
                # redirect them back to their profile
                return HttpResponseRedirect(reverse('profile'))


class NextStepView(LoginRequiredMixin, View):

    def get(self, request):
        user_steps = UserStep.objects \
                             .filter(user=request.user) \
                             .order_by("-step__number")
        if user_steps.count() == 0:
            # user hasn't started yet
            # create their first step and redirect them to it
            first_step = step=get_object_or_404(Step, number=1)
            first_user_step = UserStep(user=request.user, step=first_step)
            first_user_step.save()
            return redirect(first_user_step)
        elif (user_steps.filter(completed=True).count() == \
              Step.objects.count()):
            # user has completed the process
            # redirect them to their profile
            return redirect('profile')
        else:
            # user has completed some but not all steps
            # redirect them to the latest completed step
            return redirect(user_steps[0])
