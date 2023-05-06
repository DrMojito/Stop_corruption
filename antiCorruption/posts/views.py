from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Posts
from .forms import AddPostForm, RegisterUserForm
from .utils import DataMixin, menu


class PostIndex(DataMixin, ListView):
    model = Posts
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
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


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'posts/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавить пост")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def forum(request):
    return HttpResponse('Форум')


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Вход')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'posts/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class ShowPost(DataMixin, DetailView):
    model = Posts
    template_name = 'posts/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' +
                                      str(context['post'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class PostСategory(DataMixin, ListView):
    model = Posts
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категория - ")
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Posts.objects.filter(is_published=True,
                                    cat__slug=self.kwargs['cat_slug'])


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
