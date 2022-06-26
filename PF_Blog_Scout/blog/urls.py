from django.urls import path

from blog import views


app_name="blog"
urlpatterns = [
    #Blog

    path('', views.blogs.as_view(), name='Blogs'),
    path('blog-create', views.BlogCreateView.as_view(), name='CreateBlog'),
    path('blog/<int:pk>/update', views.BlogUpdateView.as_view(), name='BlogUpdate'),
    path('blog/<int:pk>/update_image', views.BlogUpdateImage.as_view(), name='BlogUpdateImage'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(), name='BlogDelete'),
    path('blog/<int:pk>/detail', views.BlogDetailView.as_view(), name='SingleBlog'),
    
    #Request

    path('request', views.request.as_view(), name='Request'),
    path('request-create', views.RequestCreateView.as_view(), name='CreateRequest'),
    path('request/<int:pk>/update', views.RequestUpdateView.as_view(), name='UpdateRequest'),
    path('request/<int:pk>/delete', views.RequestDeleteView.as_view(), name='DeleteRequest'),
#    path('request-django-forms', views.request_forms_django, name='RequestDjangoForms'),
    path('request/<int:pk>/vote', views.vote_request, name='request-vote'),

    #Search

    path('search', views.search),
]