from django.contrib import admin

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Настройки админки для модели About."""

    list_display = ('title', 'text')
    search_fields = ('title', 'text',)
    empty_value_display = "-пусто-"
