from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks' : tasks})
    
def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/task_edit.html', {'form': form})