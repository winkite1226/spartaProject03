from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('upload/', views.upload, name='upload'),
]