"""todo_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from todos import api_v2_views

router = routers.SimpleRouter()
router.register(r"todo_lists", api_v2_views.TodoListViewSet)


urlpatterns = [
    url(r"^todos/", include("todos.urls", namespace="todos"),),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r"^api/v1/", include("todos.api_v1_urls", namespace="apiv1"),),
    url(r"^api/v2/", include(router.urls, namespace="apiv2"),),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
