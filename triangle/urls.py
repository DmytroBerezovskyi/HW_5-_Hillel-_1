from django.urls import path

from . import views

app_name = "person"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.PersonDetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.PersonResultsView.as_view(), name="results"),
    path("create/", views.create_person, name="create-person"),
    path("update/<int:pk>/", views.update_person, name="update-person"),
    path("delete/<int:pk>/", views.delete_person, name="delete-person"),
    path("triangle/", views.triangle, name="triangle"),
]
