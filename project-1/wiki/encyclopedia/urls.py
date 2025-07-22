from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("encyclopedia/add.html", views.add, name="add"),
    path("encyclopedia/<str:title>", views.entry, name="entry")
]
