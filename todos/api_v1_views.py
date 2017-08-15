from django.shortcuts import get_object_or_404
from rest_framework import generics

from . import models
from . import serializers


class ListCreateTodoList(generics.ListCreateAPIView):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer

class RetrieveUpdateDestroyTodoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer

class ListCreateItem(generics.ListCreateAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

    def get_queryset(self):
        return self.queryset.filter(todo_list_id=self.kwargs.get("todo_list_pk"))

    def perform_create(self, serializer):
        todo_list = get_object_or_404(models.TodoList, pk=self.kwargs.get("todo_list_pk"))
        serializer.save(todo_list=todo_list)