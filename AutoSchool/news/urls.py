from . import views
from django.urls import path

urlpatterns = [
    # Переход на страницу с новостным блоком
    path('', views.news_home, name='news_home')
]