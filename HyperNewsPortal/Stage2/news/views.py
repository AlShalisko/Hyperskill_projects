

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