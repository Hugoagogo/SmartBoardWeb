from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  #The Homepage
    url(r'^(?P<channel>[0-9]+)/$', views.channel_page, name='channel'), #Page for the channel
]