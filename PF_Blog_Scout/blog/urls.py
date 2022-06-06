from django.urls import path

from blog import views


app_name="blog"
urlpatterns = [
    path('blogs', views.blogs, name='Blogs'),
    path('blog-django-forms', views.blog_forms_django, name='BlogDjangoForms'),
    path('blog/<int:pk>/', views.blog, name='SingleBlog'),
    path('request', views.request, name='Request'),
    path('request-django-forms', views.request_forms_django, name='RequestDjangoForms'),
    path('request/<int:pk>/vote', views.vote_request, name='request-vote'),
    path('users', views.users, name='users'),
    path('user-django-forms', views.user_forms_django, name='UserDjangoForms'),
    path('search', views.search),
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),

    #path('search', views.search, name='Busqueda'),
]