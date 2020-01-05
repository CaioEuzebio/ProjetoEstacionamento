from django.conf.urls import url, include
from .views import website_home


urlpatterns = [
    
    url(r'^', website_home, name='website_home'),

]
