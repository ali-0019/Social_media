from django.contrib import admin
from django.urls import path  , include

from .views import PostView , POstListView , CommentView , LikeView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    path('post-list/', POstListView.as_view(), name= 'post-list'),
    path('post/<int:pk>/comments/', CommentView.as_view(), name='comment'),
    path('post/<int:pk>/likes/', LikeView.as_view(), name='like'),
]


