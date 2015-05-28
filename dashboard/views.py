from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

import json
import datetime, calendar

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
        dtime = datetime.datetime.utcfromtimestamp(int(timestamp)+1) #+1 to allow for fractional seconds stored in db
        dtime = dtime.replace(tzinfo=timezone.utc)
        readings = readings.filter(channel=channel,datetime__gte=dtime)
    data = ((int(calendar.timegm(dt.timetuple())),v) for dt, v in readings.values_list("datetime","value"))
    return HttpResponse(json.dumps(list(data)))

def average_readings(data,period):#Average points spaced more closely than period, done with a nice generator function (lazy evaluation)
    last = 0
    total_x = 0
    total_y = 0
    count = 0
    for dt, value in data:
        if count and dt-last>period:
            yield int(total_x/count) , total_y/count
            count = 0
            total_x = 0
            total_y = 0
            last = dt
        else:
            total_x += dt
            total_y += value
            count += 1