from django.shortcuts import render
from .models import Articles


def news_home(request):
    # Сортировка записей по дате
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})