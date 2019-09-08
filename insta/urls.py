from django.urls import path

from . import  views

urlpatterns = [ 
    path('', views.PostListView.as_view(), name='post_list'), 
    path('<int:pk>/edit/',
         views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/',
         views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/delete/',
         views.PostDeleteView.as_view(), name='post_delete'),
    path('new/', views.PostCreateView.as_view(), name='post_new'),
    path('like', views.addLike, name='addLike'),  #slide7: like-ajax
    # 注意：like 不要加 /，因为index.js 中的 create_like() 跳转到的地址不含 /
]