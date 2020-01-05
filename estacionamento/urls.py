from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^sistema/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
]
