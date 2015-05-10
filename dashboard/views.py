from django.shortcuts import render, get_object_or_404

from models import Channel

def index(request):
    channels = Channel.objects.all()
    return render(request, "index.html",
                  {'channels':channels}
                  )

def channel_page(request,channel):
    channel = get_object_or_404(Channel,pk=channel)
    return render(request,"channel_page.html",
                  {"channel":channel})