from django.shortcuts import render
from django.http import JsonResponse
import json
from business.models import Shop
from customer.models import Customer
from products.models import Product
from orders.models import Orders
from delivery.models import Accepted, DeliveryAgent
from users.models import Users

def order(request, *args, **kwargs):
    if request.method == 'GET': return JsonResponse({"working":"well"})

    if request.method == 'POST':
        body = json.loads(request.body)

        shop = Shop.objects.get(id=body.get('shop_id'))
        customer = Customer.objects.get(id=body.get('customer_id'))
        pin_no = Customer.objects.get(id=body.get('customer_id')).pin_no
        product = Product.objects.get(id=body.get('product_id'))
        Orders.objects.create(shop=shop, customer=customer, product=product, pin_no=pin_no)

        return JsonResponse({"msg": "Order created successfully..."})

def accept_order(request, *args, **kwargs):
    if request.method == 'POST':
        body = json.loads(request.body)
        order = Orders.objects.get(id=body.get('order_id'))
        delivery = DeliveryAgent.objects.get(user_id=Users.objects.get(username=body.get('deliveryagent')).id)
        Accepted.objects.create(order=order, delivery_agent=delivery).save()
        
        return JsonResponse({"msg": "Order accepted successfully"})