# Generated by Django 2.2.19 on 2023-05-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230504_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='descriptions',
            field=models.TextField(default=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображения'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=199, verbose_name='Заголовок'),
        ),
    ]
