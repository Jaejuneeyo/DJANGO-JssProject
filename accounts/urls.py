from django.urls import path
from .views import signup, MyLoginView 
from django.contrib.auth.views import LogoutView #django 내장 함수 

urlpatterns = [
    path('signup/', signup, name="signup"), 
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]