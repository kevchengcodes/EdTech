from django.urls import path

from . import views

app_name = 'createproject'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('create_new_project/', views.create_new_project, name='create_new_project'),
    path('<int:proj_id>/addprojtoclass/', views.addprojtoclass, name='addprojtoclass'),
    path('home/', views.home, name='home'),
    path('<int:proj_id>/proj_detail/', views.proj_detail, name='proj_detail'),
]