from django.db import models
from users.models import Users
from orders.models import Orders
from django.core.validators import RegexValidator

class DeliveryAgent(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=15)

class Accepted(models.Model):
    delivery_agent = models.ForeignKey(DeliveryAgent, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        order = Orders.objects.get(id=self.order.id)
        order.is_accepted = True
        order.save()
        super(Accepted, self).save(*args, **kwargs)