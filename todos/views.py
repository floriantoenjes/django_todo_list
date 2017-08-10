from django.shortcuts import render

from .models import Item, TodoList

# Create your views here.
def todo_list_overview(request):
    todo_lists = TodoList.objects.all()
    return render(request, "todos/todo_list_overview.html", {"todo_lists": todo_lists})