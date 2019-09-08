from django.contrib import admin
from . import models

class CommentInline(admin.TabularInline):
    model = models.Comment

class LikeInline(admin.TabularInline):
    model = models.Like

class PostAdmin(admin.ModelAdmin):
    inlines = [ CommentInline, 
                LikeInline]

# Register your models here.

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Like)
