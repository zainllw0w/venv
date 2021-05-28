from django.contrib import admin


from django.contrib import admin
from .models import News, SummonerInfo

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'update_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class SummonerInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'summonerName', 'summonerLevel', 'mainid')
    list_display_links = ('id', 'summonerName')
    search_fields = ('summonerName', 'mainid')


admin.site.register(News, NewsAdmin)
admin.site.register(SummonerInfo, SummonerInfoAdmin)