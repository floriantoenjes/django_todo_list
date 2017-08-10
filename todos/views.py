from django.shortcuts import get_object_or_404, render

from .models import Item, TodoList

# Create your views here.
def todo_list_overview(request):
    todo_lists = TodoList.objects.all()
    return render(request, "todos/todo_list_overview.html", {"todo_lists": todo_lists})

def todo_list_detail(request, todo_list_pk):
    todo_list = get_object_or_404(TodoList, pk=todo_list_pk)
    return render(request, "todos/todo_list_detail.html", {"todo_list": todo_list})

def item_detail(request, todo_list_pk, item_pk):
    item = get_object_or_404(Item, todo_list_id=todo_list_pk, pk=item_pk)
    return render(request, "todos/item_detail.html", {"item": item})