from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import ItemForm, TodoListForm
from .models import Item, TodoList


def todo_list_overview(request):
    todo_lists = TodoList.objects.all()
    return render(request, "todos/todo_list_overview.html", {"todo_lists": todo_lists})

def todo_list_detail(request, todo_list_pk):
    todo_list = get_object_or_404(TodoList, pk=todo_list_pk)
    return render(request, "todos/todo_list_detail.html", {"todo_list": todo_list})

def todo_list_edit(request, todo_list_pk):
    todo_list = get_object_or_404(TodoList, pk=todo_list_pk)
    form = TodoListForm(instance=todo_list)

    if request.method == "POST":
        form = TodoListForm(instance=todo_list, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Created {}".format(form.cleaned_data["name"]))
            return HttpResponseRedirect(todo_list.get_absolute_url())

    return render(request, "todos/todo_list_form.html", {"form": form, "todo_list": todo_list})

def item_detail(request, todo_list_pk, item_pk):
    item = get_object_or_404(Item, todo_list_id=todo_list_pk, pk=item_pk)
    return render(request, "todos/item_detail.html", {"item": item})

@login_required
def item_create(request, todo_list_pk):
    todo_list = get_object_or_404(TodoList, pk=todo_list_pk)
    form = ItemForm()

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.todo_list = todo_list
            item.save()
            return HttpResponseRedirect(item.get_absolute_url())

    return render(request, "todos/item_form.html", {"form": form, "todo_list": todo_list})

@login_required
def item_edit(request, item_pk, todo_list_pk):
    item = get_object_or_404(Item, pk=item_pk, todo_list_id=todo_list_pk)
    form = ItemForm(instance=item)

    if request.method == "POST":
        form = ItemForm(instance=item, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated {}".format(form.cleaned_data["name"]))
            return HttpResponseRedirect(item.get_absolute_url())

    return render(request, "todos/item_form.html", {"item": item, "form": form, "todo_list": item.todo_list})