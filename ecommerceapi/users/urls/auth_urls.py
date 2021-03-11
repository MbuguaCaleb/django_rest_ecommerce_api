from django.urls import path
from users.views import authentication_views as views


urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register', views.registerUser, name='register'),

]
