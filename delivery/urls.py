from django.urls import path
from delivery.views import *

urlpatterns = [
    path("orders/",OrdersView.as_view()),
    path("create/",NewAgent.as_view()),
    path("update/<int:pk>/",UpdateAgent.as_view()),
    path("list/",OrderedItemsView.as_view()),
]