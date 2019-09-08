from django.contrib import admin
from . import models

class CommentInline(admin.TabularInline):
    model = models.Comment

class PostAdmin(admin.ModelAdmin):
    inlines = [ CommentInline, ]

# Register your models here.

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Like)
