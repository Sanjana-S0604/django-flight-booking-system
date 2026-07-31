from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home, name='home'),
    path('booknow/<int:id>/',booknow, name='booknow'),
    path('history/',history, name='history'),
    path('cancel/<int:id>/',cancel_booking, name='cancel_booking'),
    path('update/<int:id>/',update_booking, name='update_booking'),
    path('profile/',profile, name='profile'),
    path('update_profile/',update_profile, name='update_profile'),
    path('change_password/',change_password, name='change_password'),
    path('about/',about, name='about'),
    path('support/',support, name='support'),
    path('',user_login, name='user_login'),
    path('logout/',user_logout, name='user_logout'),
    path('register/',register, name='register'),
    path('bookings/',bookings, name='bookings'),
]