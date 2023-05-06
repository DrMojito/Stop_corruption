from django.urls import path

from .views import (PostIndex,
                    about,
                    news,
                    AddPost,
                    forum,
                    LoginUser,
                    RegisterUser,
                    ShowPost,
                    PostСategory,
                    logout_user,
                    FeedBackFormView,)


urlpatterns = [
    path('', PostIndex.as_view(), name='home'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('message/', AddPost.as_view(), name='message'),
    path('forum/', forum, name='forum'),
    path('contact/', FeedBackFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', PostСategory.as_view(), name='category'),
]
