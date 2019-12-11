from django.db import models

# Create your models here.
class contact(models.Model):
	name = models.CharField(max_length=30, unique=True)
	phone = models.CharField(max_length=15, unique=True)
	email = models.CharField(max_length=50, unique=True)
	address = models.CharField(max_length=50, unique=True)
	gmaps_x = models.CharField(max_length=10, unique=True)
	gmaps_y = models.CharField(max_length=10, unique=True)
	gmaps_zoom = models.CharField(max_length=2, unique=True)
	gmaps_API = models.CharField(max_length=64, unique=True)
	footer_info = models.TextField(blank=True)
	def __str__(self):
		return 'Dont create a new entry! Ara tee uut sissekannet!'

class navbar_lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	index = models.CharField(max_length=15, blank=True)
	about = models.CharField(max_length=15, blank=True)
	def __str__(self):
		return self.lang

class langs(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	flag = models.ImageField()
	def __str__(self):
		return self.lang

class social_media(models.Model):
	url = models.CharField(max_length=999, blank=True)
	icon = models.CharField(max_length=20, blank=True)
	def __str__(self):
		return self.url + ' - ' + self.icon