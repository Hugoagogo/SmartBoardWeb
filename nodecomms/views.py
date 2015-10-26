from django.shortcuts import render, get_object_or_404
from dashboard.models import Channel, PowerReading, SmartBoard, SwitchStatus
from django.http import HttpResponse, HttpResponseRedirect

import datetime

import random


def log_data(request,channel,reading):
    channel = get_object_or_404(Channel,pk=channel)
    pt = PowerReading(channel=channel, value=reading)
    pt.save()
    return HttpResponse("OK")

def log_board_data(request,board,data):
    board = get_object_or_404(SmartBoard,pk=board)
    data = data.split(",")
    for num, channel in enumerate(board.channels.order_by("channel_num")):
        pt = PowerReading(channel=channel, value=data[num])
        pt.save()
    return HttpResponse("OK")

def clear_channel(request,channel):
    channel = get_object_or_404(Channel,pk=channel)
    PowerReading.objects.filter(channel=channel).delete()
    return HttpResponse("OK")
    

def add_random(request,channel):
    channel = get_object_or_404(Channel,pk=channel)
    pt = PowerReading(channel=channel, value=random.randint(0,100))
    pt.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	
def get_status(request,board):
	board = get_object_or_404(SmartBoard, pk=board)
	status = board.current_status()
	
	return HttpResponse(status.status)

def button_press(request, channel):
    channel = get_object_or_404(Channel,pk=channel)
    status = SwitchStatus( board = channel.board,
                status = channel.board.current_status().status ^ (1<<(channel.channel_num-1)) )
    print(channel.board.current_status().status)
    status.save()

    return HttpResponse(status.status)
