"""URL for Pass_gen app"""
from django.urls import path
from . import views

app_name = 'Pass_gen'

urlpatterns = [
    path('', views.password_view, name='password'),
    # path('generate/', views.password_view, name='password'),
]