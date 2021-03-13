from django.urls import path
from .views import *
urlpatterns = [
    path('login/',user_login,name="account_home"),
    path('register/',user_registation,name="account_register"),
    path('logout/',user_logout,name="account_logout"),

]