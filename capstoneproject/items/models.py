from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100)
