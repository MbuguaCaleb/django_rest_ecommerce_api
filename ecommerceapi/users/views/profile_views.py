from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from users.models import CustomerProfile
from users.serializers import UserSerializer, UserSerializerWithToken, CustomerProfileSerializer
from rest_framework import status


# Get all the registered users
# Only accessible by admin
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# Get user profile
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# add user profile info
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCustomerProfileInfo(request):
    try:
        # user info from the JWT Token
        username = request.user
        data = request.data
        user = User.objects.get(username=username)

        serailizer = UserSerializer(user, many=False)

        addCustomerProfile = CustomerProfile.objects.create(
            user_id=serailizer.data['id'],
            mobile_no=data['mobile_no'],
            town=data['town'],
            is_active=True
        )

        serializer = CustomerProfileSerializer(addCustomerProfile, many=False)
        return Response(serializer.data)
    except:
        message = {
            'detail': 'User with this email already exists or invalid request'
        }
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
