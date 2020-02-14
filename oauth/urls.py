from django.urls import path, include

from oauth import admin
from . import views

app_name = 'oauth'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
