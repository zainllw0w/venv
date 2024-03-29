# Generated by Django 3.2.3 on 2021-05-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Обновалено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at'],
            },
        ),
    ]
