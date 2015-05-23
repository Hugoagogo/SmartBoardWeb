from django.db import models

#Defines the database setup

class SmartBoard(models.Model):
	name = models.CharField(max_length=50)
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