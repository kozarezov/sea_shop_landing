from operator import mod
from django.db import models

class About(models.Model):
    address = models.CharField('Адрес', max_length=1024)
    phone = models.CharField('Телефон', max_length=20)
    staff = models.CharField('ФИО сотрудника', max_length=50)
    text = models.TextField('Описание', help_text='Введите текст "О нас"')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.text[:15]
