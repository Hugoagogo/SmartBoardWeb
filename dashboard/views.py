from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

import json
import datetime

from .models import Channel

def index(request):
    channels = Channel.objects.all()
    return render(request, "index.html",
                  {'channels':channels} #dictionary object that is used for refference in template
                  )

def channel_page(request,channel):
    channel = get_object_or_404(Channel,pk=channel)
    return render(request,"channel_page.html",
                  {"channel":channel}) #dictionary object that is used for refference in template

def channel_data(request,channel,timestamp=None):
    channel = get_object_or_404(Channel,pk=channel)
    readings = channel.points.all().order_by("datetime")
    if timestamp != None:
        dtime = datetime.datetime.fromtimestamp(float(timestamp))
        readings = readings.filter(channel=channel,datetime__gt=dtime)
    return HttpResponse(json.dumps([(reading.datetime.isoformat(),reading.value) for reading in readings]))