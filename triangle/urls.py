from django.urls import path

from . import views

urlpatterns = [
    path("", views.triangle, name="triangle"),
    path("person/", views.person, name="person"),
    path("create_person/", views.create_person, name="create_person"),
    path("update_person/", views.update_person, name="update_person"),
]
