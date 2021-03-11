from django.urls import path
from users.views import profile_views as views


urlpatterns = [
    path('users', views.getUsers, name='users'),
    path('', views.getUserProfile, name='user-profile'),
    path('create', views.addCustomerProfileInfo,
         name='create_customer_profile')


]
