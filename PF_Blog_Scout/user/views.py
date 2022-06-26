from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import redirect,render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from user.models import Avatar
import os

from user.forms import UserRegisterForm, UserEditForm, AvatarForm


# Create your views here.

# Create your views here.
def register(request):
    if request.method == 'POST':
        print("Post")
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("form_valid")
            form.save()
            return redirect("user:user-login")
    #form = UserCreationForm()
    form = UserRegisterForm()
    print("else")
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

@login_required
def view_user(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    return render(
        request=request,
        context=context_dict,
        template_name="user/user.html",
    )

@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('user:user-view')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="user/user_form.html",
    )

@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('home:Home')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="user/avatar_form.html",
    )


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}

class users(PermissionRequiredMixin, ListView):
    permission_required = 'user.delete_user'
    model = User
    template_name = "user/user_list.html"

class UserUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'user.change_user'
    model = User
    success_url = reverse_lazy('user:Users_list')
    fields = ['first_name', 'last_name', 'email', 'is_superuser']

class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'user.change_user'
    model = User
    success_url = reverse_lazy('user:Users_list')

