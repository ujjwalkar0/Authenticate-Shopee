from django.db import models
from users.models import Users
from business.exceptions import UserTypeException
from django.core.validators import RegexValidator


class Shop(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=15)
    email_id = models.EmailField(max_length=255)
    website = models.CharField(max_length=255,blank=True,null=True)
    Pin_No = models.IntegerField(null=True,blank=True)

    def save(self, *args, **kwargs):
        if Users.objects.get(id=self.user_id.id).user_type != 'Business':
            raise UserTypeException("User type must be business")
        else:
            super(Shop, self).save(*args, **kwargs)