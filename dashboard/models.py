from django.db import models

from django.utils import timezone

#Defines the database setup

class SmartBoard(models.Model):
    name = models.CharField(max_length=50)

    def current_status(self):
        stat = self.status.filter(datetime__lt=timezone.now()).order_by("-datetime")
        if(stat.count() == 0):
            status = SwitchStatus( board = self, status = 0)
            status.save()
            return status
        return stat.first()
    def __str__(self):
        return self.name
    
class Channel(models.Model):
    board = models.ForeignKey(SmartBoard,related_name = "channels")
    channel_num = models.IntegerField()
    name = models.CharField(max_length=50)
    units = models.CharField(max_length=50,default="Power")

    def __str__(self):
        return self.name
    
class PowerReading(models.Model):
    channel = models.ForeignKey(Channel,related_name = "points")
    value = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)
    
class SwitchStatus(models.Model):
    board = models.ForeignKey(SmartBoard,related_name = "status")
    status = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)