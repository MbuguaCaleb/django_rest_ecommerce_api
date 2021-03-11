from django.urls import path
from .views import MyTokenObtainPairView, registerUser, getUsers, getUserProfile


urlpatterns = [
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register', registerUser, name='register'),
    path('profile', getUserProfile, name='user-profile'),
    path('', getUsers, name='users'),
]
