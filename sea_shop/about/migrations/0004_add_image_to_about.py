# Generated by Django 4.0.6 on 2022-07-10 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_add_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, upload_to='about/', verbose_name='Картинка'),
        ),
    ]
