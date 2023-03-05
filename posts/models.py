from django.db import models
from django.contrib.auth.models import User

category_choices = [
    ('playstation', 'Playstation'),
    ('xbox', 'Xbox'),
    ('pc', 'PC'),
    ('nintendo', 'Nintendo'),
    ('tech', 'Tech')
]


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.CharField(choices=category_choices, max_length=30)
    image = models.ImageField(
        upload_to='images/', default='../default_post_bezjcc', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'