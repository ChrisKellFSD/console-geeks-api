from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Contact(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Profile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.message