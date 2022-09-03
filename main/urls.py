from django.urls import path , include

from . import views

urlpatterns = [
path('' , views.home , name = "home"),
path('login', views.login_page , name = "login"),
path('register' , views.register , name = "register"),
path('handleSignUp' , views.handleSignUp , name= "handleSignUp"),
path('handleLogin' , views.handleLogin , name = "handleLogin"),
path("handleLogout" , views.handleLogout , name = "handleLogout"),
path("base" , views.base , name = "base"),
path("addstudent" , views.addStudent , name = "addStudent")
]