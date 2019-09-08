# insta/views.py 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from annoying.decorators import ajax_request        # slide 7 (需要预先安装 django-annoying)

from .models import Post, Like


class PostListView(LoginRequiredMixin, ListView): 
    # (slide5) 添加功能：只有 login 的用户才能看到 posts  
    model = Post
    template_name = 'post_list.html'
    login_url = "login"

    # def get_queryset(self):     # slide 8
    #     '''default: return Post.objects'''
    #     current_user = self.request.user
    #     following = set()
    #     for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
    #         following.add(conn.following)
    #     return Post.objects.filter(author__in=following)

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']       # 仅允许用户更新 title

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("post_list")
        # 注意：此时不能用reverse()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'image']    
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form) 

@ajax_request
# 定义的函数专门用于响应 ajax_request，因此不用 render 到 template 里
def addLike(request):   # non-class-based view
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, author=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, author=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }


