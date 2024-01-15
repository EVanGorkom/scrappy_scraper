from django.db import models

class Item(models.Model):
  item_name = models.CharField(max_length=255)
  item_price = models.DecimalField(max_digits=100, decimal_places=2)
  sale = models.BooleanField(default=False)
  sale_percent = models.IntegerField(default=0)
  sale_price = models.DecimalField(default=0, max_digits=100, decimal_places=2)

  def __str__(self):
    return self.item_name