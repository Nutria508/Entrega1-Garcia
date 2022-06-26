from django.urls import path
from chat import views



app_name="chat"
urlpatterns = [
    path('message-django-forms/<int:pk>', views.message_forms_django, name='MessageDjangoForms'),
    
]