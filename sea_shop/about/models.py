from django.db import models

class About(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Описание', help_text='Введите текст "О нас"')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name != 'ID':
                yield (field.verbose_name, field.value_to_string(self))
