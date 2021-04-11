from django.urls import path

from . import views

app_name = 'scrapenews'
urlpatterns = [
    path('', views.index, name='index'),
    path('log_link/', views.log_link, name='log_link'),
]