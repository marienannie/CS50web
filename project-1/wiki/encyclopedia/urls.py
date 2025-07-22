from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/add", views.add, name="add"),
    path("wiki/<str:title>", views.entry, name="entry")
]
