from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновалено')
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class SummonerInfo(models.Model):
    summonerName = models.CharField(max_length=255, verbose_name='Имя призывателя')
    profileIconId = models.IntegerField(verbose_name='ico')
    summonerLevel = models.IntegerField(verbose_name='lvl')
    puuid = models.CharField(max_length=255, verbose_name='puuid')
    accountId = models.CharField(max_length=255, verbose_name='accountId')
    mainid = models.CharField(max_length=255, verbose_name='id')
    jsonacc = models.JSONField(verbose_name='jsonacc')
    jsonrank = models.JSONField(verbose_name='jsonrank')
    jsonclash = models.JSONField(verbose_name='jsonclash')
    jsonspec = models.JSONField(verbose_name='jsonclash')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.summonerName