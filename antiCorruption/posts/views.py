from typing import Any, Dict
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Posts
from .forms import AddPostForm


menu = [{'title': "Новости", 'url_name': 'news'},
        {'title': "Добавить запись", 'url_name': 'message'},
        {'title': "Форум", 'url_name': 'forum'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Контакты", 'url_name': 'contact'},
        {'title': "Вход", 'url_name': 'login'},
        {'title': "Регистрация", 'url_name': 'registration'}]


class PostIndex(ListView):
    model = Posts
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Posts.objects.filter(is_published=True)


def about(request):
    templates = 'posts/about.html'
    context = {'title': 'О нас',
               'menu': menu}
    return render(request, templates, context=context)


def news(request):
    return HttpResponse('Новости')


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'posts/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить пост'
        return context



# def message(request):
#     templates = 'posts/addpage.html'
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     context = {'menu': menu,
#                'title': 'Добавление записи',
#                'form': form}
#     return render(request, templates, context=context)


def forum(request):
    return HttpResponse('Форум')


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Вход')


def registration(request):
    return HttpResponse('Регистрация')


class ShowPost(DetailView):
    model = Posts
    template_name = 'posts/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


class PostСategory(ListView):
    model = Posts
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Posts.objects.filter(is_published=True,
                                    cat__slug=self.kwargs['cat_slug'])


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
