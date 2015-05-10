from django.shortcuts import render, get_object_or_404
from dashboard.models import Channel, PowerReading
from django.http import HttpResponse, HttpResponseRedirect

import random


def log_data(request,channel,reading):
    channel = get_object_or_404(Channel,pk=channel)
    pt = PowerReading(channel=channel, value=reading)
    pt.save()
    return HttpResponse("OK")

def add_random(request,channel):
    channel = get_object_or_404(Channel,pk=channel)
    pt = PowerReading(channel=channel, value=random.randint(0,100))
    pt.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))