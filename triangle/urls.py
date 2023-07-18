from django.urls import path

from . import views

urlpatterns = [
    path("", views.triangle, name="triangle"),
]
