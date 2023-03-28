from django.urls import path
from contact_test import views

urlpatterns = [
    path('contact-test/', views.ContactList.as_view()),
]