from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.lists, name='articles'),
    path('articles/<id>', views.detail, name='detail'),
]