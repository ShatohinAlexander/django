from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

CATEGORIES = [
    {'slug': 'python', 'name': 'Python'},
    {'slug': 'django', 'name': 'Django'},
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': 'Docker'},
    {'slug': 'linux', 'name': 'Linux'},
]

TAGS = [
    {'slug': 'html', 'name': 'HTML'},
    {'slug': 'css', 'name': 'CSS'},
    {'slug': 'sql', 'name': 'SQL'}
]

POSTS = [
    {'slug': 'python_oop', 'title': 'Python OOP', 'text': 'Текст поста про python oop'},
    {'slug': 'django_orm', 'title': 'Django ORM', 'text': 'Текст поста про django orm'}
]

def main(request):
    catalog_categories_url = reverse("blog:categories")
    catalog_tags_url = reverse("blog:tags")

    context = {
        "title": "Главная страница",
        "text": "Текст главной страницы",
        "user_status": "moderator",
    }
    return render(request, "main.html", context)

def about(request):
    return render(request, "about.html")

def catalog_posts(request):
    links = []
    for post in POSTS:
        url = reverse('blog:post_detail', args=[post['slug']])
        links.append(f'<p><a href="{url}">{post}</a></p>')

    return HttpResponse(f'''
        <h1>Cписок всех постов</h1>
        {''.join(links)}
        <p><a href="{reverse('main')}">На главную страницу</a></p>
''')

def post_detail(request, post_slug):
    post = [post for post in POSTS if post['slug'] == post_slug]
    if post: post = post[0]
    if post:
        name = post['title']
    else:
        return HttpResponse(f'<p>Поста {post_slug} не сущетсвует</p>')

    return HttpResponse(f'''
        <h1>Пост {name}</h1>
        <p>{post['text']}</p>
        <p><a href="{reverse('blog:posts')}">Назад к постам</a></p>
        ''')

def catalog_categories(request):
    links = []
    for category in CATEGORIES:
        url = reverse('blog:category_detail', args=[category['slug']])
        links.append(f'<p><a href="{url}">{category}</a></p>')

    return HttpResponse(f'''
        <h1>Cписок всех категорий</h1>
        {''.join(links)}
        <p><a href="{reverse('blog:posts')}">К списпку постов</a></p>''')

def category_detail(request, category_slug):
    category = [cat for cat in CATEGORIES if cat['slug'] == category_slug][0]
    if category:
        name = category['name']
    else:
        name = category_slug

    return HttpResponse(f'''
        <h1>Категория {name}</h1>
        <p><a href="{reverse('blog:categories')}">Назад к категориям</a></p>
        ''')

def catalog_tags(request):
    links = []
    for tag in TAGS:
        url = reverse('blog:tags_detail', args=[tag['slug']])
        links.append(f'<p><a href="{url}">{tag}</a></p>')

    return HttpResponse(f'''
        <h1>Cписок всех тегов</h1>
        {''.join(links)}
        <p><a href="{reverse('blog:posts')}">К списпку постов</a></p>''')

def tag_detail(request, tag_slug):
    tag = [tag for tag in TAGS if tag['slug'] == tag_slug][0]
    if tag:
        name = tag['name']
    else:
        name = tag_slug

    return HttpResponse(f'''
        <h1>Тег {name}</h1>
        <p><a href="{reverse('blog:tags')}">Назад к списку тегов</a></p>
        ''')
