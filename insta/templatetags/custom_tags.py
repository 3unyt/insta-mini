import re

from django import template
from django.urls import NoReverseMatch, reverse
from insta.models import Like
from users.models import CustomUser


register = template.Library()

@register.simple_tag
def has_user_liked_post(post, author):
    try:
        like = Like.objects.get(post=post, author=author)
        return "fa-heart"
    except:
        return "fa-heart-o"

@register.simple_tag
def is_following(current_user, background_user):
    return background_user.get_followers().filter(creator=current_user).exists()