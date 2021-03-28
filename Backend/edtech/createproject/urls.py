from django.urls import path

from . import views

app_name = 'createproject'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_new_project/', views.create_new_project, name='create_new_project'),
]