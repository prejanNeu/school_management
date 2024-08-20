from django.urls import path 
from .views import login,register,dashboard,school_login

urlpatterns = [
    path("login",login,name="login"),
    path("register",register, name="register"),
    path("dashboard",dashboard,name="dashboard"),
    path("school/admin",school_login,name="school_login"),
]