from django.db import models

# Модель заполнения заявки пользователя
class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.EmailField()