from builtins import reversed

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, FormView
from apps.web import models
from apps.web import  forms
# Create your views here.

class Inicio(ListView):
    model=models.Especialidades
    template_name = "./principal/inicio.html"
    context_object_name = "home"
class AboutMe(ListView):
    model = models.About
    context_object_name = "about"
    template_name = "./principal/about-me.html"


class Servicios(ListView):
    model = models.Services
    context_object_name = "services"
    template_name = "./principal/servicios.html"

class Portafolio(ListView):
    model = models.Portafolio
    context_object_name = "portafolios"
    template_name = "./principal/portafolio.html"


class Contacto(FormView):
    form_class = forms.ContactoForm
    template_name = './principal/contacto.html'

    def form_valid(self, form):
        asunto = form.cleaned_data['asunto']
        mensaje = form.cleaned_data['mensaje']
        email = form.cleaned_data['email']
        
        recibe=['hit.mindblog@gmail.com']
        mail = EmailMessage(subject=asunto, body=mensaje,from_email=[email],to=recibe,reply_to=[email])
        try:
            mail.send()
            self.success_url=(reverse('contacto')+"?ok")
        except:
            self.success_url = (reverse('contacto') + "?fail")
            
        return super(Contacto, self).form_valid(form)

