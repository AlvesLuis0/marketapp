from django.db import models

# Create your models here.
class PERSON(models.Model):
  CPF = models.CharField(primary_key=True, max_length=11)
  USERNAME = models.CharField(max_length=50)
  PASSWORD = models.CharField(max_length=50)
  PHONE = models.CharField(max_length=22)
  PERMISSION = models.CharField(max_length=25)
  REGISTERED = models.DateTimeField()

  def __str__(self):
  	return self.NAME

class PRODUCT(models.Model):
  ID = models.AutoField(primary_key=True)
  NAME = models.CharField(max_length=50)
  PRICE = models.DecimalField(max_digits=6, decimal_places=2)
  QUANTITY = models.IntegerField(default=0)
  REGISTERED = models.DateTimeField()

  def __str__(self):
  	return self.NAME