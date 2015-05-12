from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<channel>[0-9]+)/(?P<reading>[0-9.]+)/?$', views.log_data, name='log_data'),  #Page to add datapoints
    url(r'^(?P<channel>[0-9]+)/random/?$', views.add_random, name='log_random'),            #Add a random datapoint
]