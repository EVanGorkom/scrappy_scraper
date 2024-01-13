from django.db import models

class Item(models.Model):
  item_name = models.CharField(max_length=255)
  item_price = models.DecimalField(max_digits=100, decimal_places=2)
  sale = models.BooleanField(default=False)
  sale_percent = models.IntegerField(max_digits=3)
  sale_price = models.DecimalField(max_digits=100, decimal_places=2)