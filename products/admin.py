from django.contrib import admin
from products.models import Categories, Product

admin.site.register([Categories, Product])