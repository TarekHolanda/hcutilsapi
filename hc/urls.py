from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sprints", views.sprints, name="sprints"),
    path("test", views.sprint, name="sprint"),
]
