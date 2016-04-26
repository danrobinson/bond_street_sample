from django.conf.urls import include, url
from django.contrib import admin
from flow import urls as flow_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^flow/', include(flow_urls))
]
