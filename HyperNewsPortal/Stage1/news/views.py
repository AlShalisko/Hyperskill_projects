from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def coming_soon(request):
    return render(request, 'news/ComingSoon.html')