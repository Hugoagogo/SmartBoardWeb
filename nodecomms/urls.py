from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<channel>[0-9]+)/(?P<reading>[0-9.]+)/?$', views.log_data, name='log_data'),  #Page to add datapoints
    url(r'^(?P<board>[0-9]+)/(?P<data>[0-9.,]+)/?$', views.log_board_data, name='log_board_data'),  #Page to add datapoints to board
    url(r'^(?P<channel>[0-9]+)/clear/?$', views.clear_channel, name='clear_channel'),  #Page to add datapoints to board
    #url(r'^(?P<channel>[0-9]+)/random/?$', views.add_random, name='log_random'),            #Add a random datapoint
	url(r'^status/(?P<board>[0-9]+)/?$', views.get_status, name='get_status'),  #Page to add datapoints to board
    url(r'^button/(?P<channel>[0-9]+)/?$', views.button_press, name='button_press'),  #Page to add datapoints to board
    url(r'^addboard/(?P<id>[0-9]+)/(?P<numchannels>[0-9]+)/?$', views.add_board, name='add_board'), #page to add a board object
]