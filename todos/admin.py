from django.contrib import admin

from .models import TodoList, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "order", "completed"]
    list_editable = ["order", "completed"]

admin.site.register(TodoList)
admin.site.register(Item, ItemAdmin)