from django.urls import path
from products.views import *
from django.shortcuts import redirect

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('accounts/profile/', lambda x: redirect('/', permanent=True)),
    path('add_category/', product_category),
    path('category_more_details/<int:pk>/', get_category_details),
    path('new_product/', NewProduct.as_view()),
    path('details/<int:pk>/', ProductDetailView.as_view()),
    path('update_product/<int:pk>/', UpdateProductView.as_view()),
    path('delete_product/<int:pk>/', DeleteProductView.as_view()),
    # path('new_product/', new_product),
]