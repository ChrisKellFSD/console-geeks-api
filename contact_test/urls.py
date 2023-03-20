from django.urls import path
from contact_test import views

urlpatterns = [
    path('contact/', views.CommentList.as_view()),
]