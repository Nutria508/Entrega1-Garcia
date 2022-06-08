
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from user import views

app_name="user"
urlpatterns = [
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)