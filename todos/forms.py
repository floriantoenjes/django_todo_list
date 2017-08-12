from django import forms

from . import models

class TodoListForm(forms.ModelForm):
    class Meta:
        model = models.TodoList
        fields = ["name", "order"]


class ItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ["name", "description", "order"]