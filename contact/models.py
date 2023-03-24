from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='owner_contact_form'
        )
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.message