from django.db import models

# Create your models here.
class PRODUCT(models.Model):
    NAME = models.CharField(max_length=50)
    PRICE = models.DecimalField(decimal_places=2, max_digits=6)
    QUANTITY = models.IntegerField()

    def __str__(self):
        return self.NAME