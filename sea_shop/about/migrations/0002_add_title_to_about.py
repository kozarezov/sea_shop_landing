# Generated by Django 4.0.6 on 2022-07-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_add_all_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default='', max_length=200, verbose_name='Заголовок'),
            preserve_default=False,
        ),
    ]