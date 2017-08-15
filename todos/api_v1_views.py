from rest_framework import generics

from . import models
from . import serializers

class ListCreateTodoList(generics.ListCreateAPIView):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer

class RetrieveUpdateDestroyTodoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer