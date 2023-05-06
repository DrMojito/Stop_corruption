from django.contrib import admin

from .models import Posts, Category


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'data_create',
                    'is_published'
                    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descriptions')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'data_create')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name'
                    )
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта'
admin.site.site_header = 'Админ-панель сайта'
