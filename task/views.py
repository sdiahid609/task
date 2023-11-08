from django.shortcuts import render
from .models import Task
from .forms import TaskForm #se crea como clase TaskForm para poder importarlo
from django.shortcuts import redirect


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks' : tasks})
    
def task_new(request):
    if request.method == "POST": #Dos situaciones, si el form esta vacio y cuando se envia.
        form = TaskForm(request.POST) #El form recibe el request.post
        if form.is_valid(): 
            task = form.save(commit=False)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm() #Esta creando un formulario vacío
    return render(request, 'task/task_edit.html', {'form': form})