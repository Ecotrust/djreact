from django.urls import path, include
from .views import TodoWrapper

urlpatterns = [
    path('', TodoWrapper),
]