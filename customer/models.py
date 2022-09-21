from django.db import models
from users.models import Users

class Customer(models.Model):
    name = models.ForeignKey(Users, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    pin_no = models.IntegerField()