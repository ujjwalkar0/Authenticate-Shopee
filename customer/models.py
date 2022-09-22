from django.db import models
from users.models import Users
from django.core.validators import RegexValidator

class Customer(models.Model):
    name = models.ForeignKey(Users, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    pin_no = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=15, default=None)
