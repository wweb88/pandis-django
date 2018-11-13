from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('luchadores', views.luchadores, name="luchadores"),
    path('inscripcion', views.inscripcion, name="inscripcion"),
]