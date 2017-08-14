from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)

from .forms import ItemForm, TodoListForm
from .mixins import PageTitleMixin
from .models import Item, TodoList


class TodoListListView(CreateView, ListView):
    model = TodoList
    context_object_name = "todo_lists"
    fields = ("name",)
    template_name = "todos/todo_list_overview.html"

    def form_valid(self, form):
        if  not self.request.user.is_authenticated:
            return HttpResponseForbidden
        return super(TodoListListView, self).form_valid(form)

class TodoListDetailView(PageTitleMixin, UpdateView, DetailView):
    fields = ("name", "order")
    model = TodoList
    context_object_name = "todo_list"
    template_name = "todos/todo_list_detail.html"

    def get_page_title(self):
        obj = self.get_object()
        return "{} Details".format(obj.name)

class TodoListDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    template_name = "todos/todo_list_confirm_delete.html"
    success_url = reverse_lazy("todos:todo_list_overview")


def todo_list_overview(request):
    todo_lists = TodoList.objects.all()
    total = todo_lists.aggregate(total=Count("name"))
    return render(request, "todos/todo_list_overview.html", {"todo_lists": todo_lists, "total": total})

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