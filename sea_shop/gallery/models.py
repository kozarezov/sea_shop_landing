from django.db import models

class Gallery(models.Model):
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Фото', upload_to='gallery/', blank=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.title

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name != 'ID':
                yield (field.verbose_name, field.value_to_string(self))
