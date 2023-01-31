from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('<str:slug>-p<int:pid>', show, name='show-post'),
    path('<str:slug>-c<int:cid>', show_category_posts, name='show-category-posts'),
    path('all', all_posts, name='all-posts'),
    path('bookmark', bookmark, name='bookmark'),
    path('bookmarks', bookmarks, name='bookmarks')
]
