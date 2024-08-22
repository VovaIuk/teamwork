# Generated by Django 5.1 on 2024-08-22 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Колнка',
                'verbose_name_plural': 'Колонки',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.CharField(max_length=1000, verbose_name='Описание')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.columns', verbose_name='Колонка')),
            ],
            options={
                'verbose_name': 'Карточка',
                'verbose_name_plural': 'Карточки',
                'db_table': 'cards',
            },
        ),
    ]
