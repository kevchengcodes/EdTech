from django.urls import path

from . import views

app_name = 'createclass'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('create_new_class/', views.create_new_class, name='create_new_class'),
]