from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Usuario', min_length=3)
    name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
