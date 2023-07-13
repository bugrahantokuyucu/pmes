from django.urls import path
from . import views


urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("create/", views.note_create, name="note_create"),
    path("<int:pk>/edit/", views.note_edit, name="note_edit"),
]
