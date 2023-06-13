from django.db import models

# Модель новосной записи
class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='None')
    anons = models.CharField('анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
