from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.RegisterationView,name='register'),
    path('verify/<str:token>',views.verify),
]