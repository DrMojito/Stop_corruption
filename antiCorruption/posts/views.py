from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render

from .models import Posts
from .forms import AddPostForm


menu = [{'title': "Новости", 'url_name': 'news'},
        {'title': "Добавить запись", 'url_name': 'message'},
        {'title': "Форум", 'url_name': 'forum'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Контакты", 'url_name': 'contact'},
        {'title': "Вход", 'url_name': 'login'},
        {'title': "Регистрация", 'url_name': 'registration'}]


def index(request):
    templates = 'posts/index.html'
    posts = Posts.objects.all()
    context = {'title': 'Главная странциа',
               'menu': menu,
               'posts': posts,
               'cat_selected': 0}
    return render(request, templates, context=context)


def about(request):
    templates = 'posts/about.html'
    context = {'title': 'О нас',
               'menu': menu}
    return render(request, templates, context=context)


def news(request):
    return HttpResponse('Новости')


def message(request):
    templates = 'posts/addpage.html'
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Posts.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()

    context = {'menu': menu,
               'title': 'Добавление записи',
               'form': form}
    return render(request, templates, context=context)


def forum(request):
    return HttpResponse('Форум')


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Вход')


def registration(request):
    return HttpResponse('Регистрация')


def show_post(request, post_slug):
    templates = 'posts/post.html'
    post = get_object_or_404(Posts, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, templates, context=context)


def show_category(request, cat_id):
    templates = 'posts/index.html'
    posts = Posts.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {'title': 'Категории',
               'menu': menu,
               'posts': posts}
    return render(request, templates, context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
