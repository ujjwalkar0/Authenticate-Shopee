from django.urls import path
from business.views import *

urlpatterns = [
    path('register_shop/',ShopCreateView.as_view()),
    path('register_shop/<int:pk>/',ShopUpdateView.as_view())
]
