from django.urls import path

from . import views

app_name = 'scrapenews'
urlpatterns = [
    path('home', views.index, name='index'),
    path('home2', views.index2, name='index2'),
    path('log_link/', views.log_link, name='log_link'),
    path('cognitivehome/', views.cognitivehome, name='cognitivehome'),
    path('cognitive_questionnaire/', views.cognitive_questionnaire, name='cognitive_questionnaire'),
]