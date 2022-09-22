from rest_framework.serializers import ModelSerializer
from orders.models import Orders

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"