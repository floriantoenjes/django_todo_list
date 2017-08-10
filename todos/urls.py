from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.todo_list_overview, name="todo_list_overview"),
    url(r"^(?P<todo_list_pk>\d+)/$", views.todo_list_detail, name="todo_list_detail")
]