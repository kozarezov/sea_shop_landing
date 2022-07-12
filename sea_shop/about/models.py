from distutils.command.upload import upload
from django.db import models

class About(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Описание', help_text='Введите текст "О нас"')
    image = models.ImageField('Картинка', upload_to='about/', blank=True, help_text='Изображение 1000х668 (файл не должен содержать русские символы в названии)')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name != 'ID' and field.verbose_name != 'Картинка':
                yield (field.verbose_name, field.value_to_string(self))
