from distutils.command.upload import upload
from email.mime import image
from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from datetime import datetime, date


class movie(models.Model):
    caption= models.CharField(max_length=100)
    def __str__(self):
        return self.caption
    


class Video(models.Model):
    
    caption = models.CharField(max_length=100)
    video=models.FileField(upload_to="movie/%y")
    def __str__(self):
        return self.caption

#spiderman
class VideoD(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    videod=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption
    
#uncharted
class Uncharted(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    charted=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption
    
#batman  
class Batman(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    bat=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption
    
#matrix
class Matrix(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    mat=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption
#morbius   
class Morbius(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    mob=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption
#moonfall  
class Moonfall(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    moon=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption
    
#theinbetween
class TIB(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    tib=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption
    
#turning red
class Turn(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    turn=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption
    
#Koati
class Koati(models.Model):
    
    caption = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, default=True)
    kot=models.FileField(upload_to="movie/%y")
    thumb=models.FileField(upload_to="thumb/%y", blank=True)
    views_count =models.IntegerField(default=0)
    def __str__(self):
        return self.caption

