from django.contrib import admin

from . import models


@admin.register(models.Contact)
class AboutAdmin(admin.ModelAdmin):
    """Настройки админки для модели Contact."""

    list_display = ('address', 'phone', 'staff', 'email')
    empty_value_display = "-пусто-"
