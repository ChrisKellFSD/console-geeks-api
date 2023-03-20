from django.urls import path
from contact_test import views

urlpatterns = [
    path('contact/', views.ContactList.as_view()),
]