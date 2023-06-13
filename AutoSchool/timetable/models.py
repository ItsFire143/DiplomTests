import users.models
from django.db import models


# Таблица для записей на практическое вождение
class Schedule(models.Model):
    instructor = models.ForeignKey('Instructors', on_delete=models.PROTECT)
    weekday = models.ForeignKey('Weekdays', on_delete=models.PROTECT)
    time = models.ForeignKey('Hours', on_delete=models.PROTECT)
    user = models.CharField('Пользователь', max_length=100)

    class Meta:
        verbose_name = 'Запись на практику'
        verbose_name_plural = 'Записи на практику'


# Таблица инструкторов
class Instructors(models.Model):
    fullName = models.CharField('ФИО', max_length=250)


#Таблица дней недели
class Weekdays(models.Model):
    weekdayName = models.CharField('Дни недели', max_length=15)


#Таблица часов
class Hours(models.Model):
    hourPieces = models.CharField('Часы', max_length=10)