from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import News, SummonerInfo
import requests


class SummonerInfoView(DetailView):
    model = SummonerInfo
    context_object_name = 'lolname'
    template_name = 'searcher/info.html'



def clashTeam(json, reg, api):
    IDteam = json[0]['teamId']
    URL = f'https://{reg}.api.riotgames.com/lol/clash/v1/teams/{IDteam}?api_key={api}'
    response = requests.get(URL)
    res = response.json()
    name = res['name']
    ico = res['iconId']
    tier = res['tier']
    abbreviation = res['abbreviation']
    players = res['players']
    return name, ico, tier, abbreviation, players


def api_lol(name='zainllw0w'):
    region = 'ru'
    api = 'RGAPI-bda8f014-4ea8-460e-8aec-d7f73fc62d47'
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + api
    response = requests.get(URL)
    res = response.json()
    ID = res['id']
    ID = str(ID)
    ico = res['profileIconId']
    lvl = res['summonerLevel']
    puuid = res['puuid']
    accountId = res['accountId']
    URL2 = 'https://' + region + '.api.riotgames.com/lol/league/v4/entries/by-summoner/' + ID + '?api_key=' + api
    response = requests.get(URL2)
    itog = response.json()
    if itog[1]['queueType'] == 'RANKED_SOLO_5x5':
        i_solo = 1
        i_flex = 0
    else:
        i_solo = 0
        i_flex = 1
    tier = itog[i_solo]['tier']
    division = itog[i_solo]['rank']
    point = itog[i_solo]['leaguePoints']
    wins_solo = itog[i_solo]['wins']
    losses_solo = itog[i_solo]['losses']
    games_solo = wins_solo + losses_solo
    wins_flex = itog[i_flex]['wins']
    losses_flex = itog[i_flex]['losses']
    games_flex = wins_flex + losses_flex
    tier_f = itog[i_flex]['tier']
    division_f = itog[i_flex]['rank']
    point_f = itog[i_flex]['leaguePoints']
    wr_solo = wins_solo / games_solo * 100
    wr_solo = round(wr_solo)
    wr_flex = wins_flex / games_flex * 100
    wr_flex = round(wr_flex)
    summonerName = name
    URL3 = f'https://{region}.api.riotgames.com/lol/clash/v1/players/by-summoner/{ID}?api_key={api}'
    response = requests.get(URL3)
    jsonclash = response.json()
    URL4 = f'https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{ID}?api_key={api}'
    response = requests.get(URL4)
    jsonspec = response.json()
    if not jsonclash:
        clashPosition = None
        teamName = 'Нет команды'
        teamIco = 0
        teamTier = None
        abbreviation = None
        players =None
    else:
        clashPosition = jsonclash[0]['position']
        teamName, teamIco, teamTier, abbreviation, players = clashTeam(jsonclash, region, api)
    context = {
        'teamName': teamName,
        'teamIco': teamIco,
        'teamTier': teamTier,
        'abbreviation': abbreviation,
        'players': players,
        'title': f'Профиль {summonerName}',
        'ico': ico,
        'lvl': lvl,
        'puuid': puuid,
        'accountId': accountId,
        'id': ID,
        'jsonacc': res,
        'jsonrank': itog,
        'jsonclash': jsonclash,
        'jsonspec': jsonspec,
        'tier': tier,
        'division': division,
        'point': point,
        'name': summonerName,
        'wins_s': wins_solo,
        'losses_s': losses_solo,
        'games_s': games_solo,
        'wins_f': wins_flex,
        'losses_f': losses_flex,
        'games_f': games_flex,
        'tier_f': tier_f,
        'division_f': division_f,
        'point_f': point_f,
        'wr_solo': wr_solo,
        'wr_flex': wr_flex,
        'itog': itog,
        'clashPosition': clashPosition,
    }
    return context


def index(request):
    if request.method == 'POST':
        context = api_lol(name=request.POST.get('name'))

        
        return render(request, template_name='searcher/info.html', context=context)
    return render(request, template_name='searcher/index.html')


def news(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Новости и обновления проекта'
    }
    return render(request, template_name='searcher/news.html', context=context)


def info(request):
    if request.method == 'POST':
        context = api_lol(name=request.POST.get('name'))
        try:
            SummonerInfo.objects.get(summonerName=context['name'])
            context['check'] = 'есть'
        except SummonerInfo.DoesNotExist:
            context['check'] = 'нету'
            SummonerInfo.objects.create(summonerName= context['name'],
                                        profileIconId= context['ico'],
                                        summonerLevel= context['lvl'],
                                        puuid= context['puuid'],
                                        accountId= context['accountId'],
                                        mainid= context['id'],
                                        jsonacc= context['jsonacc'],
                                        jsonrank= context['jsonrank'],
                                        jsonclash= context['jsonclash'],
                                        jsonspec= context['jsonspec'],
                                        slug= context['name'])
        return render(request, template_name='searcher/info.html', context=context)
    context = api_lol(name='zainllw0w')
    return render(request, template_name='searcher/info.html', context=context)


def timeline(request):
    context = {
        'news': news,
        'title': 'Новости и обновления проекта'
    }
    return render(request, template_name='searcher/timeline.html', context=context)
