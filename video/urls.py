from django.urls import path, include
from . import views

app_name = 'Video'

urlpatterns = [
    path('', views.video, name='video'),
]
