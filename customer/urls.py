from django.urls import path
from customer.views import *

urlpatterns = [
    path('register_customer/', RegisterCustomerView.as_view()),
    path('update_customer/<int:pk>', UpdateCustomerView.as_view()),
]