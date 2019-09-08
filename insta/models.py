from django.db import models
from django.conf import settings
from django.urls import reverse
from imagekit.models import ProcessedImageField
from users.models import CustomUser
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
        CustomUser,
        on_delete=models.CASCADE,
        related_name='my_posts'     
            # use `user.my_posts` to get all posts from the user
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    def get_like_count(self):       # slide 7
        return self.likes.count()
    
    def get_comment_count(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',    # set the name of this reverse relationship
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('post_list')


class Like(models.Model):
    '''
    like1 <- yutingsun like post1
    like2 <- test like post2
    post.likes -> (like1, like2)  # 返回所有给 post1 点赞的关系
    yutingsun.likes -> like1      # 返回 yutingsun 点赞的关系

    '''
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE, # post 被删除时，like 的关系也被删除
        related_name='likes',  
        )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('post', 'author')
    
    def __str__(self):
        return 'Like: ' + self.author.username + ' likes ' + self.post.title