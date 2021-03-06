# Generated by Django 3.1.7 on 2021-02-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('short_description', models.CharField(max_length=200, verbose_name='Краткое описание')),
                ('price', models.CharField(max_length=10, verbose_name='Цена')),
                ('picture', models.ImageField(upload_to='', verbose_name='Картинка')),
            ],
        ),
    ]
