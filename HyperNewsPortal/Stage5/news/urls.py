from django.urls import path
from . import views

urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
    path('news/<int:post_id>/', views.article, name='article'),
    path('news/', views.main, name='main'),
    path('news/create/', views.create, name='create'),
]