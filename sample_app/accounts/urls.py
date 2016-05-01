from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'profile', 
        RedirectView.as_view(url=reverse_lazy('flow_index'))),
    url(r'^', include('registration.backends.simple.urls'))
]