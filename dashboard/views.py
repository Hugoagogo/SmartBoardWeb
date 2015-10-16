from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

import json
import datetime, calendar

from .models import Channel, SmartBoard

def index(request):
    boards = SmartBoard.objects.all()
    channels = Channel.objects.all()
    return render(request, "index.html",
                  {'channels':channels,
                   'boards':boards} #dictionary object that is used for refference in template
                  )

def channel_page(request,channel,timeframe=None):
    channel = get_object_or_404(Channel,pk=channel)
    
    timestamp_start = 0
    #if timeframe != None:
    #    timestamp_start = calendar.timegm(datetime.datetime.utcnow().timetuple())
    if timeframe == "hour":
        timestamp_start = 60*60
    elif timeframe == "5minutes":
        timestamp_start = 5*60
    elif timeframe == "day":
        timestamp_start = 60*60*24

    status = channel.board.current_status()
    
    return render(request,"channel_page.html",
                  {"channel":channel,
                   "timestart":timestamp_start,
                   "status":status}) #dictionary object that is used for refference in template

def channel_data(request,channel,timestamp=None):
    channel = get_object_or_404(Channel,pk=channel)
    readings = channel.points.all().order_by("datetime")
    
    if timestamp != None:
        dtime = datetime.datetime.utcfromtimestamp(int(timestamp)+1) #+1 to allow for fractional seconds stored in db
        dtime = dtime.replace(tzinfo=timezone.utc)
        readings = readings.filter(channel=channel,datetime__gte=dtime)
    
    readings = readings.values_list("datetime","value")
    
    # Convert the readings into something simpler than a query set
    # Note the use of iterator() and round braces around the expression so it is a generator (lazy evaluation)
    data = ((int(calendar.timegm(dt.timetuple())),v) for dt, v in readings.iterator())
    
    # if we have too many values cut them down to once every 20 seconds max (temprary fix to not being able to display all data on website)
    if readings.count() > 20000:
        data = average_readings(data,20)
    
    return HttpResponse(json.dumps(list(data)))

def average_readings(data,period):#Average points spaced more closely than period, done with a nice generator function (lazy evaluation)
    last = 0
    total_x = 0
    total_y = 0
    count = 0
    for timestamp, value in data:
        if count and timestamp-last>period:
            yield int(total_x/count) , total_y/count
            count = 1
            total_x = timestamp
            total_y = value
            last = timestamp
        else:
            total_x += timestamp
            total_y += value
            count += 1