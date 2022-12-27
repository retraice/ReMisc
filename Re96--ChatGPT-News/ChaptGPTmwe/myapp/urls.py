# myapp/urls.py

from django.urls import path, include # include added by Re, Matthes p. 395
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('myapp.urls')), # added by Jeffre    
]
