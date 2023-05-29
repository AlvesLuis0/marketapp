from django.db import models

# Create your models here.
class PRODUCT(models.Model):
    NAME = models.CharField(max_length=50, blank=False)
    PRICE = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    QUANTITY = models.IntegerField(max_length=5, blank=False)

    def __str__(self):
        return self.NAME