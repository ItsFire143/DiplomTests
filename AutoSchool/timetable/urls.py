from django.urls import path, include
from . import views

urlpatterns = [
    # Переход на страницу расписания
    path('', views.getUser, name='timetable')
]