from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category
from .constants import POSTS_PER_PAGE


def get():
    """Получение постов из БД."""
    return Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    """Главная страница / Лента записей."""
    return render(request, 'blog/index.html', {'post_list': get()[:POSTS_PER_PAGE]})


def post_detail(request, id):
    """Отображение полного описания выбранной записи."""
    post = get_object_or_404(get(), id=id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Отображение публикаций категории."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    context = {'category': category,
               'post_list': get().filter(category=category)}
    return render(request, 'blog/category.html', context)
