from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home),
    path('result', views.result),
    path('error', views.error),
    path('candidates', views.candidates),
]
