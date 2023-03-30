from django.urls import path
from .import views

urlpatterns = [
    path("", views.getNotes, name="notes-list"),
    path("<int:pk>/", views.notes_detail),
]
