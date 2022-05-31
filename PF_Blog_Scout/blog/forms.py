import datetime
from turtle import title
from django import forms
from django.forms import ModelForm



class BlogForm(forms.Form):
    title = forms.CharField(max_length=20, min_length=3, label='Titulo')
    subtitle = forms.CharField(max_length=30, label='Subtitulo')
    autor = forms.CharField(max_length=30, min_length=3, label='Autor')
    text = forms.CharField(max_length=120, min_length=3, label='Texto')
    post_date = forms.DateField(
        label='Fecha de posteo',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )



class UserForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre')
    last_name = forms.CharField(max_length=20, min_length=3, label='Apellido')
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(max_length=20, label='Contraseña')



class RequestForm(forms.Form):
    text = forms.CharField(max_length=50, label="Pedido")
    date = forms.DateField(
        label='Fecha de pedido',
        widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
    )
    