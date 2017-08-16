from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from todos import models, serializers
from todos.models import Item


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer

    @detail_route(methods=["get"])
    def items(self, request, pk=None):
        items = Item.objects.filter(todo_list_id=pk)
        serializer = serializers.ItemSerializer(items, many=True)
        return Response(serializer.data)