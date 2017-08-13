from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.TodoListListView.as_view(), name="todo_list_overview"),
    url(r"^(?P<todo_list_pk>\d+)/$", views.TodoListDetailView.as_view(), name="todo_list"),
    url(r"^(?P<todo_list_pk>\d+)/edit_todo_list/$", views.todo_list_edit, name="edit_todo_list"),
    url(r"^(?P<todo_list_pk>\d+)/create_item/$", views.item_create, name="create_item"),
    url(r"^(?P<todo_list_pk>\d+)/(?P<item_pk>\d+)/$", views.item_detail, name="item"),
    url(r"^(?P<todo_list_pk>\d+)/edit_item/(?P<item_pk>\d+)/$", views.item_edit, name="edit_item"),
]