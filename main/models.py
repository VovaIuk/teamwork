from tabnanny import verbose
from django.db import models


class Columns(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='Название')


    class Meta:
        db_table = 'product'
        verbose_name = 'Колнка'
        verbose_name_plural = 'Колонки'


class Cards(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    column = models.ForeignKey(Columns, on_delete=models.PROTECT, verbose_name='Колонка')


    class Meta:
        db_table = 'cards'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'




