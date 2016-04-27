from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from .views import ProfileView

urlpatterns = [
    url(r'profile', 
        ProfileView.as_view(), name='profile'),
    url(r'^', include('registration.backends.simple.urls'))
]