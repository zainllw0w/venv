from django.urls import path
from .views import info, SummonerInfoView

urlpatterns = [
    path('', info),
    path('SummonerName=<slug:slug>/', SummonerInfoView.as_view(), name='lolname'),
]