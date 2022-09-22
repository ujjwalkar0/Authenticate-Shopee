from django.urls import path
from orders.views import *

urlpatterns = [
    path('add/', order),
    path('accept/', accept_order)
]