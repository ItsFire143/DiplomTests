from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

# Доступ к списку пользователей в панели администратора
@admin.register(User)
class UserAdmin(UserAdmin):
    pass