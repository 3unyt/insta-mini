import re

from django import template
from django.urls import NoReverseMatch, reverse
from insta.models import Like


register = template.Library()

@register.simple_tag
def has_user_liked_post(post, author):
    try:
        like = Like.objects.get(post=post, author=author)
        return "fa-heart"
    except:
        return "fa-heart-o"