# myproject/urls.py

from django.contrib import admin
from django.urls import path, include # included added by Re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')), # added by Re, Matthes p. 395
]
