from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/add", views.add, name="add"),
    path("wiki/random", views.random_page, name="random"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("error", views.error, name="error"),
    path("search", views.search, name="search")
]
