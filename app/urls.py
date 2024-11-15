from django.urls import path
from .import views

urlpatterns = [
    path("",views.login,name="login"),
    path("home/",views.home,name="home"),
    path("reg/",views.reg,name="reg"),
    path("logout/",views.logout,name="logout"),
     
]
