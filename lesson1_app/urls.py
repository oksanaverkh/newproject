from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heads_and_tails/<int:throws_number>', views.heads_and_tails, name='heads_and_tails'),
    path('dice/<int:throws_number>', views.dice, name='dice'),
    path('random_number/<int:throws_number>', views.random_number, name='random_number'),
    path('authors/', views.authors_view, name='authors'),
    path('author_posts/<int:author_id>', views.author_posts, name='author_posts'),
    path('posts/', views.posts_view, name='posts'),
    path('post_full/<int:post_id>', views.post_full, name='post_full'),
    path('about/', views.about, name='about'),
    path('game/', views.choose_game, name='game'),
    path('author/', views.author_add, name='author'),
    path('post/', views.post_add, name='post'),
]
