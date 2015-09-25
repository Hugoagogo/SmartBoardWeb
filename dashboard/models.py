from django.db import models

import datetime

#Defines the database setup

class SmartBoard(models.Model):
	name = models.CharField(max_length=50)

	def current_status(self):
		return self.status.filter(datetime__lt=datetime.datetime.utcnow()).order_by("-datetime").first()
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