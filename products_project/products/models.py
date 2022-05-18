from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255,blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quantity = models.IntegerField()

    