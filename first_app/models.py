from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):
    Name = models.CharField(max_length =200)
    Organism = models.CharField(max_length =200)
    number = models.IntegerField()
    Email = models.EmailField(max_length =100)
    Address = models.CharField(max_length =200)


class Formation(models.Model):
    Number = models.PositiveIntegerField()
    Domain = models.CharField(max_length=200)
    Mode = models.CharField(max_length =200)
