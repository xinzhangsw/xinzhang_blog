from django.urls import path
from . import views

app_name = 'guestbook'
urlpatterns = [
    path('message/', views.message, name='message'),
    path('save/', views.save, name='save')
]
