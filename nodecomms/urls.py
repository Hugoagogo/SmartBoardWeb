from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^(?P<channel>[0-9]+)/(?P<reading>[0-9.]+)/?$', views.log_data, name='log_data'),
    url(r'^(?P<channel>[0-9]+)/random/?$', views.add_random, name='log_random'),
]