from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Панель администратора
    path('admin/', admin.site.urls),
    # Главная страница
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Переход в приложение пользователей
    path('users/', include('users.urls')),
    # Переход в приложение новостного блока
    path('news/', include('news.urls')),
    # Переход в приложение дополнительных страниц
    path('frames/', include('frames.urls')),
    # Переход на приложение расписаний
    path('timetable/', include('timetable.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Подключение статик файлов
