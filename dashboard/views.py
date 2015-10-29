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

def board_page(request,board,timeframe=None):
    board = get_object_or_404(SmartBoard,pk=board)
    channels = Channel.objects.all().filter(board = board)
    
    timestamp_start = 0
    #if timeframe != None:
    #    timestamp_start = calendar.timegm(datetime.datetime.utcnow().timetuple())
    if timeframe == "hour":
        timestamp_start = 60*60
    elif timeframe == "5minutes":
        timestamp_start = 5*60
    elif timeframe == "day":
        timestamp_start = 60*60*24

    status = board.current_status()
    
    return render(request,"board_page.html",
                  {"board":board,
                   "channels":channels,
                   "timestart":timestamp_start,
                   "status":status}) #dictionary object that is used for refference in template

def channel_data(request,channel,timestamp=None):
    channel = get_object_or_404(Channel,pk=channel)
    readings = channel.points.all().order_by("datetime")
    
    if timestamp != None:
        dtime = datetime.datetime.utcfromtimestamp(int(timestamp)+1) #+1 to allow for fractional seconds stored in db
        dtime = dtime.replace(tzinfo=timezone.utc)
        readings = readings.filter(datetime__gte=dtime)
    
    readings = readings.values_list("datetime","value")
    
    # Convert the readings into something simpler than a query set
    # Note the use of iterator() and round braces around the expression so it is a generator (lazy evaluation)
    data = ((int(calendar.timegm(dt.timetuple())),v) for dt, v in readings.iterator())
    
    # if we have too many values cut them down to once every 20 seconds max (temprary fix to not being able to display all data on website)
    if readings.count() > 20000:
        data = average_readings(data,20)
    
    return HttpResponse(json.dumps(list(data)))

def board_data(request,board,timestamp=None):
    board = get_object_or_404(SmartBoard,pk=board)
    readings = [channel.points.all().order_by("datetime") for channel in board.channels.all()]
    
    
    if timestamp != None:
        dtime = datetime.datetime.utcfromtimestamp(int(timestamp)+1) #+1 to allow for fractional seconds stored in db
        dtime = dtime.replace(tzinfo=timezone.utc)
        readings = [channel.filter(datetime__gte=dtime) for channel in readings]
    
    # Convert the readings into something simpler than a query set
    # Note the use of iterator() and round braces around the expression so it is a generator (lazy evaluation)
    
    readings = [((int(calendar.timegm(dt.timetuple())),v) for dt, v in channel.values_list("datetime","value").iterator()) for channel in readings]
    
    simlified = squish_readings(readings);
    
    #Dont worry about this for now we wont have that much data
    #for index in range(len(readings)):
    #    # if we have too many values cut them down to once every 20 seconds max (temprary fix to not being able to display all data on website)
    #    if readings[index].count() > 20000:
    #        readings[index] = average_readings(readings[index],20)
    
    return HttpResponse(json.dumps(list(simlified)))

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
            
def squish_readings(readings):
    line = [next(c,None) for c in readings] # Use line to store all of the oldest value in each channel
    while any(i!=None for i in line): # keep going till we run out of points
        t = min(i[0] for i in line if i is not None) # get our smallest time
        yield [t] + [i[1] if i != None and i[0] == t else None for i in line] # return a line with only values from the smallest time
        line = [i if i == None or i[0] != t else next(c,None) for i, c in zip(line, readings)] # bump the values we just sent out of line so we dont sent them again

    
