from rest_framework import serializers

from . import models


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "created_at",
            "order"
        )

        model = models.TodoList