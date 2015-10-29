from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  #The Homepage
    url(r'^(?P<channel>[0-9]+)/(?P<timeframe>\b5minutes\b|\bhour\b|\bday\b)?$', views.channel_page, name='channel'), #Page for the channel
    url(r'^(?P<channel>[0-9]+)/data/(?:(?P<timestamp>[0-9]+)/)?$', views.channel_data, name='channel_data'), #Page for the channel
    url(r'^board/(?P<board>[0-9]+)/(?P<timeframe>\b5minutes\b|\bhour\b|\bday\b)?$', views.board_page, name='board'), #Page for the channel
    url(r'^(?P<board>[0-9]+)/data-board/(?:(?P<timestamp>[0-9]+)/)?$', views.board_data, name='board_data'), #Page for the channel
]