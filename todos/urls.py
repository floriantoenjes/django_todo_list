from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.todo_list_overview, name="todo_list_overview"),
    url(r"^(?P<todo_list_pk>\d+)/$", views.todo_list_detail, name="todo_list"),
    url(r"^(?P<todo_list_pk>\d+)/create_item/$", views.item_create, name="create_item"),
    url(r"^(?P<todo_list_pk>\d+)/(?P<item_pk>\d+)/$", views.item_detail, name="item"),
]