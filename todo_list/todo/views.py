from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

def index(request):
    tasks = TodoItem.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

def delete_task(request, task_id):
    task = TodoItem.objects.get(id=task_id)
    task.delete()
    return redirect('index')

def update_task(request, task_id):
    task = TodoItem.objects.get(id=task_id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=task)
    return render(request, 'update_task.html', {'form': form})
