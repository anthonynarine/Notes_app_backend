from django.urls import path
from .import views

urlpatterns = [
    path("", views.notes_list),
    path("<int:pk>/", views.notes_detail),
]
