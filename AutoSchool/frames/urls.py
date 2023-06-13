from . import views
from django.urls import path

urlpatterns = [
    # Переход на страницу подачи заявки
    path('apps/', views.applications, name='apps'),
    # Переход на страницу с контактными данными
    path('contacts/', views.contact, name='contacts'),
    # Переход на страницу с информацией об образовательной организацией
    path('org/', views.org, name='org'),
    # Переход на страницу с программами обучения
    path('progr/', views.programs, name='programs'),
    # Переход на страницу с данными об автошколе
    path('school/', views.shcool, name='school')
]