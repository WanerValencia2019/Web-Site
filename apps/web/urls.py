from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from apps.web import views

urlpatterns = [
    path('',views.Inicio.as_view(),name="inicio"),
    path('about/',views.AboutMe.as_view(),name="about"),
    path('services/',views.Servicios.as_view(),name="services"),
     path('portafolio/',views.Portafolio.as_view(),name="portafolio"),
    path('contacto/', views.Contacto.as_view(), name="contacto"),
]