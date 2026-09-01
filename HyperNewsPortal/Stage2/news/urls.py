from django.urls import path
from . import views

urlpatterns = [
    path('', views.coming_soon, name='coming_soon'),
    path('<int:post_id>/', views.article, name='article'),
]