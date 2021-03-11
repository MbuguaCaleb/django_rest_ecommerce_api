from rest_framework import serializers
from users.serializers import CustomerProfileSerializer
from .models import Orders
from users.models import CustomerProfile


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        # Return all fields from my serializer
        fields = "__all__"


class CustomerOrdersSerializer(serializers.ModelSerializer):
    customer = OrdersSerializer(many=True, read_only=True)

    class Meta:
        model = CustomerProfile
        fields = ['user_id', 'mobile_no', 'town', 'is_active', 'customer']
