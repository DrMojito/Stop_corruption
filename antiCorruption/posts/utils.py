from .models import Category
from django.db.models import Count

menu = [{'title': "Новости", 'url_name': 'news'},
        {'title': "Добавить запись", 'url_name': 'message'},
        {'title': "Форум", 'url_name': 'forum'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Контакты", 'url_name': 'contact'}]


class DataMixin:
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('posts'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
