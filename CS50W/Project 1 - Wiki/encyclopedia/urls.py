from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.content, name="content"),
    path("random", views.random_page, name="random"),
    path("search", views.query, name="search"),
    path("new", views.new_entry, name="new" ),
    path("edit/wiki/<str:entry>", views.edit, name="edit")
]
