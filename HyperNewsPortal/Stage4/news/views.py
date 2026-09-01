# Create your views here.
from django.conf import settings
import json
from datetime import datetime
from django.shortcuts import render, redirect

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

def create(request):
    if request.method == 'POST':
        with open(settings.NEWS_JSON_PATH, 'r') as file:
            news = json.load(file)

        title = request.POST.get('title')
        text = request.POST.get('text')

        links = [item['link'] for item in news]
        new_link = max(links) + 1 if links else 1

        new_item = {
            'created': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            'text': text,
            'title': title,
            'link': new_link
        }

        news.append(new_item)

        with open(settings.NEWS_JSON_PATH, 'w') as file:
            json.dump(news, file, indent=2)

        return redirect('/news/')

    return render(request, 'news/create.html')