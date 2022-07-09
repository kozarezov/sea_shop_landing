from django.contrib import admin
from . import models

@admin.register(models.Catalog)
class AboutAdmin(admin.ModelAdmin):
    """Настройки админки для модели Catalog.""" 

    list_display = ('name', 'category', 'price', 'sale', 'text')
    search_fields = ('name', 'category',)
    list_editable = ('category',)
    empty_value_display = "-пусто-"
