from django.contrib import admin

from .models import TodoList, Item


class ItemAdmin(admin.ModelAdmin):
    list_filter = ["completed"]
    list_display = ["name", "todo_list", "order", "completed"]
    list_editable = ["order", "todo_list", "completed"]
    search_fields = ["name", "description"]

admin.site.register(TodoList)
admin.site.register(Item, ItemAdmin)