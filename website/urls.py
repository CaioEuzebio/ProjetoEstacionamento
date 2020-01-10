from django.conf.urls import url, include
from .views import website_home, contato


urlpatterns = [
    
    url(r'^$', website_home, name='website_home'),
    url(r'^contato$', contato, name='contato'),

]
