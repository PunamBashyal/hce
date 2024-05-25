from django.db import models
#from categories.models import Category
class Costomer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=100,default=0)
    #username = models.CharField(max_length=100)
   # hobby = models.TextField(default='na')    

    def __str__(self):
        return self.name

# Create your models here.
