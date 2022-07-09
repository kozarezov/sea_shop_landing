from django.db import models

class Catalog(models.Model):
    CATEGORY = [
        ('Замороженная продукция', 'Замороженная продукция'),
        ('Свежие дары моря', 'Свежие дары моря'),
        ('Закуски', 'Закуски'),
    ]

    name = models.CharField('Название', max_length=200)
    category = models.CharField('Категория', choices=CATEGORY, max_length=200, blank=True)
    price = models.IntegerField('Цена')
    sale = models.IntegerField('Размер скидки %', help_text='Введите размер скидки в %', blank=True)
    text = models.TextField('Описание товара', blank=True)
    image = models.ImageField('Фото', upload_to='catalog/', blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name != 'ID':
                yield (field.verbose_name, field.value_to_string(self))
