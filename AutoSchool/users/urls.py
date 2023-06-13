from django.urls import path, include
from .views import Register

urlpatterns = [
    # Переход на список стандартных функций регистрации django
    path('', include('django.contrib.auth.urls')),
    # Переход на страницу регистрации
    path('register/', Register.as_view(), name='register')
]