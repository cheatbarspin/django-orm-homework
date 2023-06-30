from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    category = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку')
    release_date = models.DateField(verbose_name='Дата создания')
    last_change_date = models.DateField(verbose_name='Дата последнего изменения')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Фото')

    def __str__(self):
        return f'{self.name} ({self.price})'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)
