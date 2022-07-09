from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='news/', blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name != 'ID':
                yield (field.verbose_name, field.value_to_string(self))

