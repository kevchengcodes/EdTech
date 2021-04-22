from django.urls import path

from . import views

app_name = 'addpost'
urlpatterns = [
    path('createpost/', views.createpost, name='createpost'),
    path('createprojpost/', views.createprojpost, name='createprojpost'),
]