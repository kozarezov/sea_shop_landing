from django.db import models
from sorl.thumbnail import ImageField

class Catalog(models.Model):
    CATEGORY = [
        ('Замороженная продукция', 'Замороженная продукция'),
        ('Свежие дары моря', 'Свежие дары моря'),
        ('Закуски', 'Закуски'),
    ]

    name = models.CharField('Название', max_length=200)
    category = models.CharField('Категория', choices=CATEGORY, max_length=200, blank=True)
    price = models.IntegerField('Цена')
    price_category = models.CharField('Категория цены', max_length=20, help_text='Текст для описания цены (за кг / за шт / за 100г.)')
    text = models.TextField('Описание товара', blank=True)
    image = ImageField('Фото', upload_to='catalog/', blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name != 'ID':
                yield (field.verbose_name, field.value_to_string(self))
