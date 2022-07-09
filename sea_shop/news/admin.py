from django.contrib import admin

from . import models

@admin.register(models.News)
class AboutAdmin(admin.ModelAdmin):
    """Настройки админки для модели News.""" 

    list_display = ('title', 'text')
    search_fields = ('title',)
    empty_value_display = "-пусто-"

