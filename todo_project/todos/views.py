from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Todo


def todo_list(request):
    """Display all todos"""
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})


def create_todo(request):
    """Create a new todo"""
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")

        if title:
            Todo.objects.create(title=title, description=description)
        return redirect("todo_list")

    return render(request, "todos/create_todo.html")


def update_todo(request, pk):
    """Update an existing todo"""
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("description", "")
        todo.completed = request.POST.get("completed") == "on"
        todo.save()
        return redirect("todo_list")

    return render(request, "todos/update_todo.html", {"todo": todo})


def delete_todo(request, pk):
    """Delete a todo"""
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.delete()
        return redirect("todo_list")

    return render(request, "todos/delete_todo.html", {"todo": todo})


def toggle_complete(request, pk):
    """Toggle todo completion status"""
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=pk)
        todo.completed = not todo.completed
        todo.save()
        return JsonResponse({"status": "success", "completed": todo.completed})

    return JsonResponse({"status": "error"}, status=400)
