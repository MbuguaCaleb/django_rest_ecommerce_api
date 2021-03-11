from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Orders
from .serializers import OrdersSerializer, CustomerOrdersSerializer
from users.serializers import UserSerializer, CustomerProfileSerializer
from utils.sms import SMS
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
        orderName = data['order_name']

        # get user info details from the token
        user = User.objects.get(username=username)
        userSerializer = UserSerializer(user, many=False)
        userId = userSerializer.data['id']
        userName = userSerializer.data['name']

        # get Customer Details
        customer = CustomerProfile.objects.get(user_id=userId)
        customerSerializer = CustomerProfileSerializer(customer, many=False)

        # customer Info
        customerId = customerSerializer.data['user_id']
        customerTown = customerSerializer.data['town']
        customerMobile = customerSerializer.data['mobile_no']

        customerOrderInfo = Orders.objects.create(
            customer_id=customerId,
            order_name=orderName)

        # Trigger AfricasTaking SMS
        message = f'Dear {userName} ,You have ordered {orderName} to be delivered at {customerTown}'

        sendSMS = SMS(message, customerMobile)

        # sendSMS
        sendSMS.send()

        customerOrder = OrdersSerializer(
            customerOrderInfo, many=False)

        return Response(customerOrder.data, status=status.HTTP_200_OK)
    except:
        message = {
            'detail': 'Internal Server Error!'
        }
        return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
