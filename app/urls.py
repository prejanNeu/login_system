from . import views 
from django.urls import path 

urlpatterns =[
    path("",views.home,name="home"),
    path("login/", views.login_view, name="login_view"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("register/",views.register,name='register')
]