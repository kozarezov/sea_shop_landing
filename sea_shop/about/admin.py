from django.contrib import admin

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Настройки админки для модели About."""

    list_display = ('address', 'phone', 'staff', 'text')
    search_fields = ('text',)
    empty_value_display = "-пусто-"
