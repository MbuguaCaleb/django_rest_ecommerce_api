from django.urls import path
from .views import createCustomerOrder

urlpatterns = [
    path('create', createCustomerOrder, name='create-order'),

]
