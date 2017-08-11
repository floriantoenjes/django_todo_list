from django.core.urlresolvers import reverse
from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order",]

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    todo_list = models.ForeignKey(TodoList)

    class Meta:
        ordering = ["order",]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("todos:item", kwargs={
            "todo_list_pk": self.todo_list.pk,
            "item_pk": self.pk
        })