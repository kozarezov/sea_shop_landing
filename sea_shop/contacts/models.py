import email
from django.db import models

class Contact(models.Model):
    address = models.CharField('Адрес', max_length=1024)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Почта')
    staff = models.CharField('ФИО сотрудника', max_length=50)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address[:15]

    def __iter__(self):
        for field in self._meta.fields:
            if field.verbose_name != 'ID':
                yield (field.verbose_name, field.value_to_string(self))
