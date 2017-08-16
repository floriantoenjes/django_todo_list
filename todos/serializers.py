from rest_framework import serializers

from . import models


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "created_at",
            "order"
        )
        model = models.TodoList

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "description",
            "created_at",
            "completed",
            "order",
            "todo_list"
        )
        model = models.Item