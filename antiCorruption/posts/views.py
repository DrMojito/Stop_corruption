from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import Posts, Category

menu = [{'title': "Новости", 'url_name': 'news'},
        {'title': "Сообщения", 'url_name': 'message'},
        {'title': "Форум", 'url_name': 'forum'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Контакты", 'url_name': 'contact'},
        {'title': "Вход", 'url_name': 'login'},
        {'title': "Регистрация", 'url_name': 'registration'}]


def index(request):
    templates = 'posts/index.html'
    posts = Posts.objects.all()
    cats = Category.objects.all()
    context = {'title': 'Главная странциа',
               'menu': menu,
               'posts': posts,
               'cats': cats,
               'cat_selected': 0}
    return render(request, templates, context)


def about(request):
    templates = 'posts/about.html'
    context = {'title': 'О нас',
               'menu': menu}
    return render(request, templates, context)


def news(request):
    return HttpResponse('Новости')


def message(request):
    return HttpResponse('Сообщения')


def forum(request):
    return HttpResponse('Форум')


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Вход')


def registration(request):
    return HttpResponse('Регистрация')


def show_post(request, post_id):
    return HttpResponse(f'Пост №{post_id}')


def show_category(request, cat_id):
    templates = 'posts/index.html'
    posts = Posts.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {'title': 'Категории',
               'menu': menu,
               'posts': posts,
               'cats': cats}
    return render(request, templates, context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
