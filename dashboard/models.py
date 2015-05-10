from django.db import models

class SmartBoard(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name
	
class Channel(models.Model):
	board = models.ForeignKey(SmartBoard)
	channel_num = models.IntegerField()
	name = models.CharField(max_length="50")
	
	def __unicode__(self):
		return self.name
	
class PowerReading(models.Model):
	channel = models.ForeignKey(Channel,related_name = "points")
	value = models.FloatField()
	datetime = models.DateTimeField(auto_now_add=True)