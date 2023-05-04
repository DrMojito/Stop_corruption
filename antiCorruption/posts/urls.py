from django.urls import path

from .views import PostIndex, about, news, AddPost, forum, contact, login, registration, ShowPost, PostСategory


urlpatterns = [
    path('', PostIndex.as_view(), name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('message/', AddPost.as_view(), name='message'),
    path('forum/', forum, name='forum'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostСategory.as_view(), name='category'),
]
