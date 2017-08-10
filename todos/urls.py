from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.todo_list_overview, name="todo_list_overview"),
]