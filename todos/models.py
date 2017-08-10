from django.db import models

# Create your models here.
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
    todoList = models.ForeignKey(TodoList)

    class Meta:
        ordering = ["order",]

    def __str__(self):
        return self.name