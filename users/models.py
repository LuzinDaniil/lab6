from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    birthday = models.DateField(null=False, blank=True)
    #sex = models.CharField(choices=('М', 'Ж'), max_length=1, default='M')
    phone = models.CharField(max_length=20, null=False, blank=False)
    # tbd


class Order(models.Model):
    user = models.CharField(max_length=255, unique=True)
    rate = models.IntegerField(default='0')
    city = models.CharField(max_length=255, null=False, blank=False)
    street = models.CharField(max_length=255, null=False, blank=False)
    house = models.CharField(max_length=10, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    delivery_time = models.DateField(blank = True)
    comment = models.TextField(max_length=2000)

class Goods_Models(models.Model):
    name = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=10)
    price = models.IntegerField()