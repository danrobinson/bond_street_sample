from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from .models import Step

class StepView(LoginRequiredMixin, View):

    def get(self, request, step_number):
        step_int = int(step_number)
        step = get_object_or_404(Step, step_number=step_int)
        context = {
            "step_number": step_int
        }
        return render(request, 'flow/step.html', context)