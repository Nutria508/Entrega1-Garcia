from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from user.models import Avatar

# Create your views here.

from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from user.forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request=request,
                context={"mensaje": "Usuario Registrado satisfactoriamente."},
                template_name="user/login.html",
            )
    # form = UserCreationForm()
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="user/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home:Home")
        else:
            template_name = "user/login.html"
        return render(
            request=request,
            context={'form': form},
            template_name=template_name,
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="user/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("home:Home")