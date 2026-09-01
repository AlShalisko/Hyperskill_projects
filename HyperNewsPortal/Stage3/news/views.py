

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
import json

def coming_soon(request):
    return render(request, 'news/ComingSoon.html')

def article(request, post_id):
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        news = json.load(file)

    for list_item in news:
        if list_item['link'] == post_id:
            return render(request, 'news/article.html', list_item)


def main(request):
    with open(settings.NEWS_JSON_PATH, 'r') as file:
        news = json.load(file)

    news_dict = {}

    for item in news:
        date = item['created'].split()[0]

        if date not in news_dict:
            news_dict[date] = []

        news_dict[date].append(item)

    news_dict = dict(sorted(news_dict.items(), reverse=True))

    for date in news_dict:
        news_dict[date].sort(key=lambda item: item['title'])

    return render(request, 'news/MainPage.html', {'news': news_dict})