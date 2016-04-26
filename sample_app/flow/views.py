from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class StepView(View):

    def get(self, request, step_number):
        step_int = int(step_number)
        context = {
            "step_number": step_int
        }
        return render(request, 'flow/step.html', context)