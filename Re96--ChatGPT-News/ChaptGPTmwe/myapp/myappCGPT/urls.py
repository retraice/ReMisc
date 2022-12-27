# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('myapp.urls')), # added by Jeffre    
]
