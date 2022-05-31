from django.urls import path

from blog import views


app_name="blog"
urlpatterns = [
    path('', views.index, name='Home'),
    path('blogs', views.blogs, name='blogs'),
    path('blog-django-forms', views.blog_forms_django, name='BlogDjangoForms'),
    path('request', views.request, name='request'),
    path('request-django-forms', views.request_forms_django, name='RequestDjangoForms'),
    path('users', views.users, name='users'),
    path('user-django-forms', views.user_forms_django, name='UserDjangoForms'),
    path('search', views.search),

    #path('search', views.search, name='Busqueda'),
]