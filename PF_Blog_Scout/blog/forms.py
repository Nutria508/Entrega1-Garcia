from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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
    votes = forms.IntegerField (label="Votos",
        widget=forms.TextInput(attrs={'placeholder': '1'})
        )




#class UserRegisterForm(UserCreationForm):
#
#    username = forms.CharField(label='Usuario', min_length=3)
#    name = forms.CharField(label='Nombre', min_length=3)
#    last_name = forms.CharField(label='Apellido', min_length=3)
#    email = forms.EmailField(label='Correo electrónico')
#    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
#
#    class Meta:
#        model = User
#        fields = ['username', 'name', 'last_name', 'email', 'password1', 'password2']
#        help_texts = {k: "" for k in fields}
#