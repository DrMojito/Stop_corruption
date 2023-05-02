from django.urls import path

from .views import index, about, news, message, forum, contact, login, registration, show_post, show_category


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('message/', message, name='message'),
    path('forum/', forum, name='forum'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
