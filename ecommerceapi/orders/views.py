from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Orders
from .serializers import OrdersSerializer, CustomerOrdersSerializer
from users.serializers import UserSerializer, CustomerProfileSerializer
from users.models import CustomerProfile
from rest_framework import status
from django.http import JsonResponse

# Create an order


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCustomerOrder(request):
    try:
        # user info from the JWT Token
        username = request.user

        # request info
        data = request.data

        # get user object from the token
        user = User.objects.get(username=username)
        userSerializer = UserSerializer(user, many=False)

        # get user id to query from customers
        userId = userSerializer.data['id']

        customer = CustomerProfile.objects.get(user_id=userId)

        customerSerializer = CustomerProfileSerializer(customer, many=False)

        # getting customerId
        customerId = customerSerializer.data['user_id']

        customerOrderInfo = Orders.objects.create(
            customer_id=customerId,
            order_name=data['order_name']
        )

        customerOrder = OrdersSerializer(
            customerOrderInfo, many=False)

        return Response(customerOrder.data, status=status.HTTP_200_OK)
    except:
        message = {
            'detail': 'Internal Server Error!'
        }
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
