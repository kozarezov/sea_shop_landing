# Generated by Django 4.0.6 on 2022-07-10 09:26

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_add_all_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='catalog/', verbose_name='Фото'),
        ),
    ]