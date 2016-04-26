from django.http import HttpResponse
from django.views.generic import View

class StepView(View):

    def get(self, request, step_number):
        step_int = int(step_number)
        return HttpResponse("Viewing step " + step_number)