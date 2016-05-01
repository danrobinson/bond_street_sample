from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.db import transaction
from .models import Step, UserStep


class FlowView(LoginRequiredMixin, TemplateView):
    """Base class for all views that display a user's steps."""

    def get_queryset(self):
        """Get a list of the user's steps."""
        return UserStep.objects.select_related('step') \
                               .filter(user=self.request.user) \
                               .order_by('step__number')

    def get_context_data(self, **kwargs):
        """Adds a list of the user's steps into the context."""
        context = super(FlowView, self).get_context_data(**kwargs)
        context['user_steps'] = self.get_queryset()
        return context


class StepView(FlowView):
    """View for a single step.

    The get() handler is entirely taken care of by the inheritance.

    If we did write it out, it would look like:

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
    """

    template_name = 'flow/step.html'

    def get_object(self):
        """Get the step being viewed or modified."""
        step_number = self.kwargs.get('step_number')
        user_step = get_object_or_404(self.get_queryset(),
                                      step__number=int(step_number))
        return user_step

    def get_context_data(self, **kwargs):
        """Adds the step being viewed to the context."""
        context = super(StepView, self).get_context_data(**kwargs)
        context['user_step'] = self.get_object()
        return context

    @transaction.atomic
    def post(self, request, **kwargs):
        """Mark the step as completed and redirect the user appropriately."""
        user_step = self.get_object()
        user_steps = self.get_queryset()
        # if the form had any information, we'd validate and save it here
        user_step.completed = True
        user_step.save()
        # determine where to redirect the user
        later_steps = Step.objects.filter(number__gt=user_step.step.number)
        if user_steps.filter(completed=False).exists():
            # the user has later steps in progress
            # redirect them to their last step
            return redirect(user_steps.get(completed=False))
        elif Step.objects.count() == user_steps.count():
            # the user has completed all steps
            # redirect them to the index page
            return redirect('flow_index')
        else:
            # there are still additional steps to be completed
            # create the next step and redirect the user to it
            return redirect(UserStep.objects.create(step=later_steps[0],
                                                    user=request.user))


class IndexView(FlowView):

    template_name = 'flow/index.html'

    def get_context_data(self, **kwargs):
        """Insert a boolean showing whether the application is complete."""
        context = super(IndexView, self).get_context_data(**kwargs)
        total_number_of_steps = Step.objects.count()
        number_completed = self.get_queryset().filter(completed=True).count()
        context['completed'] = (total_number_of_steps == number_completed)
        return context


class ClearView(LoginRequiredMixin, View):

    def get(self, request, **kwargs):
        """Delete all of the user's steps."""
        UserStep.objects.filter(user=request.user).delete()
        return redirect('flow_index')


class StartView(LoginRequiredMixin, View):

    def get(self, request, **kwargs):
        """Get or create the user's first step."""
        first_step = Step.objects.get(number=1)
        first_user_step, created = UserStep.objects \
                                           .get_or_create(step=first_step,
                                                          user=request.user)
        return redirect(first_user_step)
