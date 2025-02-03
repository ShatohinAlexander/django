from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .blog_data import dataset
from .models import Post, Category, Tag

def main(request):
    # catalog_categories_url = reverse("blog:categories")
    # catalog_tags_url = reverse("blog:tags")

    context = {
        "title": "Главная страница",
        "text": "Текст главной страницы",
        "user_status": "moderator",
    }
    return render(request, "main.html", context=context)

def about(request):
    return render(request, "about.html")

def catalog_posts(request):
    posts = Post.objects.all()
    context = {
            'posts': posts
    }
    return render(request, 'python_blog/blog.html', context=context)

def post_detail(request, post_slug):
    post = None
    for item in Post.objects.all():
        if item.slug == post_slug:
            post = item
    if post is None:
        return render(request, '404.html')
    
    context = {
        'post': post
    }
    return render(request, 'python_blog/post_detail.html', context=context)

def catalog_categories(request):
    categories = Category.objects.all()
    categories_count = {cat.name:cat.posts.count() for cat in categories}
    context = {
        'categories': categories,
        'categories_count': categories_count
    }
    return render(request, 'python_blog/catalog_categories.html', context=context)
    

def category_detail(request, category_slug):
    category = [cat for cat in CATEGORIES if cat['slug'] == category_slug][0]
    if category:
        name = category['name']
    else:
        name = category_slug
    context = {
        'name': name
    }
    return render(request, 'python_blog/category_detail.html', context=context)

def catalog_tags(request):
    context = {
        'tags': TAGS
    }
    return render(request, 'python_blog/tags_catalog.html', context=context)

def tag_detail(request, tag_slug):
    tag = [tag for tag in TAGS if tag['slug'] == tag_slug][0]
    if tag:
        name = tag['name']
    else:
        name = tag_slug

    context = {
        'name': name
    }
    return render(request, 'python_blog/tag_detail.html', context=context)

