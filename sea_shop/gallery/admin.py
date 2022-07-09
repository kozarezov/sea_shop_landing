from django.contrib import admin

from . import models

@admin.register(models.Gallery)
class AboutAdmin(admin.ModelAdmin):
    """Настройки админки для модели Gallery.""" 

    list_display = ('title',)
    search_fields = ('title',)
    empty_value_display = "-пусто-"
