from django.urls import path
from .views import createCustomerOrder, getUserOrders

urlpatterns = [
    path('create', createCustomerOrder, name='create-order'),
    path('get', getUserOrders, name='get-orders'),

]
