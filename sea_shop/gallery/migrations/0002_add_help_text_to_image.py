# Generated by Django 3.2.10 on 2022-07-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_add_all_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, help_text='Изображение 400х400 (файл не должен содержать русские символы в названии)', upload_to='gallery/', verbose_name='Фото'),
        ),
    ]
