from django.contrib import admin
from delivery.models import DeliveryAgent, Accepted

admin.site.register([DeliveryAgent, Accepted])