from django.db import models
from products.models import Product
from business.models import Shop
from customer.models import Customer

class Orders(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pin_no = models.IntegerField()
    is_accepted = models.BooleanField(default=False, null=True)