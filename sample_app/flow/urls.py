from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'step/next$', views.NextStepView.as_view(), name='next_step'),
    url(r'step/(?P<step_number>\d+)$', views.StepView.as_view(), name='step'),
]