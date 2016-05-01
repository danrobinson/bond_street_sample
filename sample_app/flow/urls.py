from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'step/(?P<step_number>\d+)$', views.StepView.as_view(), name='flow_step'),
    url(r'start', views.StartView.as_view(), name='flow_start'),
    url(r'clear', views.ClearView.as_view(), name='flow_clear'),
    url(r'$', views.IndexView.as_view(), name='flow_index'),
]