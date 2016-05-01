from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView

from flow import urls as flow_urls
from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^flow/', include(flow_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^favicon.ico', 
        RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('flow_index')))
]
