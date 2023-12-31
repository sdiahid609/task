from django.shortcuts import render
from .models import Task
from .forms import TaskForm #se crea como clase TaskForm para poder importarlo
from django.shortcuts import redirect, get_object_or_404
from django.views import View

class task_list(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task/task_list.html', {'tasks' : tasks})

class task_new(View):
    form = TaskForm()
    def get(self, request):
        self.form = TaskForm() #Esta creando un formulario vacío
        return render(request, 'task/task_new.html', {'form': self.form}) #Si falla algun campo, redirije a la misma pagina con el formulario lleno
    def post(self, request):
        self.form = TaskForm(request.POST) #El form recibe el request.post
        if self.form.is_valid(): 
            self.form.save() 
            return redirect('task_list')
        return render(request, 'task/task_new.html', {'form': self.form}) #Si falla algun campo, redirije a la misma pagina con el formulario lleno

class task_details(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task/task_details.html', {'task' : task})
    
class task_edit(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        print("Hola")
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        print("Hola")

"""
class task_new(View):
    form = TaskForm()
    def get(self, request):
        self.form = TaskForm() #Esta creando un formulario vacío
        return render(request, 'task/task_edit.html', {'form': self.form}) #Si falla algun campo, redirije a la misma pagina con el formulario lleno
    def post(self, request):
        self.form = TaskForm(request.POST) #El form recibe el request.post
        if self.form.is_valid():
            title = self.form.cleaned_data["title"]
            description = self.form.cleaned_data["description"]
            checkBox = self.form.cleaned_data["checkBox"]
            nuevaTask = Task(title=title, description=description, checkBox=checkBox)
            nuevaTask.save()
            return redirect('task_list')
        return render(request, 'task/task_edit.html', {'form': self.form}) #Si falla algun campo, redirije a la misma pagina con el formulario lleno
"""  



