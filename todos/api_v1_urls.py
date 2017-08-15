from django.conf.urls import url

from . import api_v1_views


urlpatterns = [
    url(r"^$", api_v1_views.ListCreateTodoList.as_view(), name="todo_list_overview"),
]