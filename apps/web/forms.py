from django import forms
from django.core.validators import EmailValidator



class ContactoForm(forms.Form):
    email=forms.EmailField(required=True)
    asunto=forms.CharField(required=True)
    mensaje=forms.CharField(required=True)