from django.urls import path
from python_blog.views import catalog_posts,post_detail,catalog_categories,category_detail,catalog_tags,tag_detail,post_create

app_name = 'blog'

urlpatterns = [
    path('', catalog_posts, name = 'posts'),
# Формы поста
    path('post_create/', post_create, name='post_create'),
# Категории
    path('categories/', catalog_categories, name = 'categories'),
    path('categories/<slug:category_slug>/', category_detail, name = 'category_detail'),
# Теги
    path('tags/', catalog_tags, name = 'tags'),
    path('tags/<slug:tag_slug>/', tag_detail, name = 'tag_detail'),
# Посты
    path('<slug:post_slug>/', post_detail, name = 'post_detail'),
]