from django.db import models
from djongo import models

class Blog(models.Model):
    username=models.TextField(max_length=150)
    text= models.TextField(max_length=150)
    place= models.TextField(max_length=50,null=True)
    class Meta:
        verbose_name_plural = 'blog'
# from unittest.util import _MAX_LENGTH
# Create your models here.
# class signin(models.Model):
#     id = models.ObjectIdField()
#     Username = models.CharField(max_length=250, blank=False,unique=True)
#     Password = models.CharField(max_length=250, blank=False,unique=True)

#     FaviouriteCity = models.CharField(max_length=200, blank=False,unique=True)
#     Rating = models.IntegerField(blank=False,unique=False,default=0)
#     def str(self):
#            return self.Username
    
#     class Meta:
#         verbose_name_plural = "Contact"