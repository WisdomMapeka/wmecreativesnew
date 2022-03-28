from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<str:slug>/', views.article, name='article'),
    path('article-list/<str:category>/', views.article_list, name='article_list'),
    path('save_comment/', views.save_comment, name='save_comment'),
    path('like_dislike_comment/<str:val>/<int:comment_id>/', views.like_dislike_comment, name='like_dislike_comment'),
    # contacts
    path('sendmessage/', views.sendmessage, name='sendmessage'),
    path('contacts/', views.contacts, name='contacts',)
]
