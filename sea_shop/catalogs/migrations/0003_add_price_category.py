# Generated by Django 4.0.6 on 2022-07-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0002_change_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='price_category',
            field=models.CharField(default='за шт', help_text='Текст для описания цены (за кг / за шт / за 100г.', max_length=20, verbose_name='Категория цены'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catalog',
            name='sale',
            field=models.IntegerField(blank=True, default=0, help_text='Введите размер скидки в %', verbose_name='Размер скидки %'),
        ),
    ]
