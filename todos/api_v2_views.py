from rest_framework import viewsets

from todos import models, serializers


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer