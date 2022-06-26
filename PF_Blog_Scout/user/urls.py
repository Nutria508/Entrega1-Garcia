
from django.urls import path
from user import views

app_name="user"
urlpatterns = [
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('signup', views.register, name='user-register'),
    path('profile', views.view_user, name='user-view'),
    path('update-user', views.user_update, name='current-user-update'),
    path('load-avatar', views.avatar_load, name='avatar-load'),
    path('users', views.users.as_view(), name='Users_list'),
    path('user/<int:pk>/update', views.UserUpdateView.as_view(), name='UserUpdate'),
    path('blog/<int:pk>/delete', views.UserDeleteView.as_view(), name='UserDelete'),
]
