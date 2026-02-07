from django.urls import path
from products.views import *
from django.shortcuts import redirect

app_name = 'products'

urlpatterns = [
    path('accounts/profile/', lambda x: redirect('/', permanent=True)),
    path('add_category/', product_category),
    path('category_more_details/<int:pk>/', get_category_details),
    path('new_product/', NewProduct.as_view(), name='new_product'),
    path('details/<int:pk>/', ProductDetailView.as_view(), name='details'),
    path('update_product/<int:pk>/', UpdateProductView.as_view(), name='update'),
    path('delete_product/<int:pk>/', DeleteProductView.as_view(), name='delete'),
    path('predict/', predicted_price, name='predict'),
    path("product_api/<int:pk>/", ProductsApi.as_view(), name='api'),
]