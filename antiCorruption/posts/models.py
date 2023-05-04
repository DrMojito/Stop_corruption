from django.db import models
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=199,
                             verbose_name="Заголовок")
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name='URL')
    descriptions = models.TextField(default=True,
                                    verbose_name="Описание")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',
                              verbose_name="Изображения",
                              null=True,
                              blank=True)
    data_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True,
                                       verbose_name="Публикация")
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT,
                            verbose_name="Категория")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Публикации'
        verbose_name_plural = 'Публикации'
        ordering = ['data_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100,
                            db_index=True,
                            verbose_name="Категория")
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id', 'name']
