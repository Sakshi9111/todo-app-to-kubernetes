from django.urls import path

from . import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("create/", views.create_todo, name="create_todo"),
    path("update/<int:pk>/", views.update_todo, name="update_todo"),
    path("delete/<int:pk>/", views.delete_todo, name="delete_todo"),
    path("toggle/<int:pk>/", views.toggle_complete, name="toggle_complete"),
]
