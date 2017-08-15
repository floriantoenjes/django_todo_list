from django.conf.urls import url

from . import api_v1_views


urlpatterns = [
    url(r"^$", api_v1_views.ListCreateTodoList.as_view(), name="todo_list_overview"),
    url(r"^(?P<pk>\d+)/$", api_v1_views.RetrieveUpdateDestroyTodoList.as_view(), name="todo_list_detail"),
    url(r"^(?P<todo_list_pk>\d+)/items/$", api_v1_views.ListCreateItem.as_view(), name="item_list"),
]