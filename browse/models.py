from django.db import models
from datetime import datetime 
# Create your models here.
class browse_lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	header = models.CharField(max_length=999, blank=True)
	def __str__(self):
		return self.lang

class picture(models.Model):
	name = models.CharField(max_length=999, blank=True)
	date = models.DateTimeField(default=datetime.now, blank=True)
	category = models.CharField(max_length=999, blank=True)
	img = models.ImageField(blank=True)
	priority = models.IntegerField(default=0)
	def __str__(self):
		return self.name+" - "+str(self.date)+" - "+self.category+" - p:"+str(self.priority)

class category(models.Model):
	name = models.CharField(max_length=999, unique=True)
	def __str__(self):
		return self.name