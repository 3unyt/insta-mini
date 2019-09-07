from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ProcessedImageField

class CustomUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
        )