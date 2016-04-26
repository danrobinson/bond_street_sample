from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'step/(?P<step_number>\d+)$', views.StepView.as_view(), name='step'),
]