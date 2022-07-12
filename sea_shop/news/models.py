from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='news/', blank=True, help_text='Изображение 400х266 (файл не должен содержать русские символы в названии)')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-pub_date',)


    def __str__(self):
        return self.title

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name != 'ID':
                yield (field.verbose_name, field.value_to_string(self))

