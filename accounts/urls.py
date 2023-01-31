from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.accounts, name='signup'),
    path('login/',views.loginUser, name='login'),
]
