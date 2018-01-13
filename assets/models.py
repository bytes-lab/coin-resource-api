from datetime import datetime
from django.db import models

# Create your models here.
from django.utils import formats


class Asset(models.Model):
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=200, default='')
    image_url = models.CharField(max_length=200, default='')
    amount = models.DecimalField(max_digits=32, decimal_places=8, default=0.00)
    currency = models.CharField(max_length=10, default='')
    price_type = models.CharField(max_length=10, default='')
    buy_price = models.DecimalField(max_digits=20, decimal_places=12, default=0.00)
    purchase_price = models.DecimalField(max_digits=32, decimal_places=12, default=0.00)
    sell_price = models.DecimalField(max_digits=20, decimal_places=8, default=0.00)
    transaction_date = models.DateField(default=datetime.now, blank=True)
    note = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-transaction_date',)

    def __str__(self):
        return self.name


class SoldAssets(models.Model):
    name = models.CharField(max_length=256)
    symbol = models.CharField(max_length=200, default='')
    image_url = models.CharField(max_length=200, default='')
    asset_id = models.CharField(max_length=2, default='')
    purchase_price = models.DecimalField(max_digits=32, default=0.00, decimal_places=8)
    amount = models.DecimalField(max_digits=32, decimal_places=8, default=0.00)
    sell_price = models.DecimalField(max_digits=20, decimal_places=12, default=0.00)
    buy_price = models.DecimalField(max_digits=20, decimal_places=12, default=0.00)
    market_price = models.DecimalField(max_digits=20, decimal_places=12, default=0.00)
    currency = models.CharField(max_length=10, default='')
    price_type = models.CharField(max_length=10, default='')
    transaction_date = models.DateField(blank=True)
    note = models.CharField(max_length=256, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
