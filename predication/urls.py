from django.urls import path
from . import views

app_name = 'predication'


urlpatterns = [
    path('tuberculose', views.tuberculose, name='tuberculosePage'),
]
