# Generated by Django 3.2.10 on 2022-07-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_add_pub_date_ro_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, help_text='Изображение 400х266 (файл не должен содержать русские символы в названии)', upload_to='news/', verbose_name='Фото'),
        ),
    ]
