from django.db import models

# Create your models here.
class Dog(models.Model):
  name = models.CharField(max_length=20)
  breed = models.CharField(max_length=20)
  chip_number = models.IntegerField()

  # To add later?
  # owner FK 1:m
  # favorite foods m:m
