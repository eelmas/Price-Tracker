from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.TextField()
    amount = models.IntegerField()
    # quantity = models.IntegerField(default=1)
    category = models.CharField(max_length=255)
    store = models.CharField(max_length=255)
    score = models.FloatField()
