#App level URLs!

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('chatbot.html', views.chatbot, name='chatbot'),
    path('getResponse/', views.getResponse, name='getResponse'),
    path('add/', views.add_post, name='add_post'),
]