from django.db import models
from django.conf import settings
from django.urls import reverse
from imagekit.models import ProcessedImageField

# Create your models here.

class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
        )
    date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='my_posts'     
            # use `user.my_posts` to get all posts from the user
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
