from django.db import models

# Create your models here.

class Shop(models.Model):
    name= models.CharField(max_length=50)
    description= models.TextField()
    price = models.IntegerField()
    color = models.CharField(max_length=30)
    quantiy = models.IntegerField()
    image = models.ImageField()


