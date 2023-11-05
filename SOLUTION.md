Crear un .gitignore:

    *.pyc
    *~
    __pycache__
    entornoTask
    db.sqlite3
    /static
    .DS_Store

He creado un entorno virtual poniendo: 
```console
python3 -m venv entornoTask
```

He iniciado el entorno virtual: 
```console
source entornoTask/bin/activate
```

Crear el requeriments.txt y añadir django: Django~=4.2.7
Se puede actualizar asi: 
```console
pip install --upgrade django
```

Luego he instalado lo que habia en requirements.txt: 
```console
pip install -r requirements.txt 
```
Crear mysite
```console
django-admin startproject mysite . 
```

En settings.py, encuentra la línea que contiene TIME_ZONE y modifícala para elegir tu zona horaria. Por ejemplo:

```python
TIME_ZONE = 'Europe/Berlin'
```

Si quieres un idioma diferente, cambia el código de idioma cambiando la siguiente línea:

```python
LANGUAGE_CODE = 'es-es'
```

También tenemos que añadir una ruta para archivos estáticos. (Veremos todo acerca de archivos estáticos y CSS más adelante.) Ve al final del archivo, y justo debajo de la entrada STATIC_URL, añade una nueva llamada STATIC_ROOT:
```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

ALLOWED_HOSTS = ['127.0.0.1']
```

Crear base de datos:
```console
python manage.py migrate 
```
Iniciar servidor:
```console
python manage.py runserver 
```

Ahora crearemos nuestra aplicación: 
```console
python manage.py startapp task
```

La añadimos en mysite/settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task',
]
```

En models.py he puesto lo siguiente: 
```python
from django.db import models

class Task(models.Model):
    task = models.TextField()
    checkBox = models.BooleanField(default=False)

    def __str__(self):
        return self.task
```

Actualizar modelo en base de datos:
```console
python manage.py makemigrations task
python manage.py migrate task
```

Adminastrador de Django
```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

Crear superusuario:

```console
python manage.py createsuperuser
```

Añadimos la url de la app en mysite/urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
]
```

Creamos el archivo task/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
]
```

Creamos la vista en task/views.py

```python
from django.shortcuts import render

def task_list(request):
    return render(request, 'task/task_list.html', {})
```

Hay que hacer una migración:

```console
python manage.py makemigrations task
python manage.py migrate task
```

Entramos en la consola de Django

```console
python manage.py shell
```

Importamos task.models

```console
from task.models import Task
```

Vemos todas las Tasks:

```console
Task.objects.all()
```

En views.py añadimos las tasks:

```python
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks' : tasks})
```

Creamos templates/task/task_list.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Task list</title>
  </head>
  <body>
    {% for task in tasks %} 
        <p>{{ task.title }}</p>
        <p>{{ task.description }}</p>
        <p>{{ task.checkBox }}</p>
    {% endfor %}
  </body>
</html>

Creamos task/forms.py

```python
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'text',)
```
task_list.html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Task list</title>
  </head>
  <body>
    <h1>Tasks</h1>
    <a href="{% url 'task_new' %}"><p>Añadir nueva tarea</p></a>
    <hr>
    {% for task in tasks %} 
        <h2>{{ task.title }}</h2>
        <p>{{ task.description }}</p>
        <p>{{ task.checkBox }}</p>
        <hr>
    {% endfor %}
  </body>
</html>

urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/new/', views.task_new, name='task_new'),
]
```

forms.py

```python
from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description',)
```

views.py

```python
from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks' : tasks})
    
def task_new(request):
    form = TaskForm()
    return render(request, 'task/task_edit.html', {'form': form})
```

templates/task_edit.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task edit</title>
</head>
<body>
    <h1>Task edit</h1>
    <hr>
    <h2>New task</h2>
    <form method="POST" class="task-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
</body>
</html>

Para que se guarden las tasks, en views.py:

```python
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
            task.title = request.user
            task.description = request.user
            task.save()
            return redirect('task_list', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'task/task_edit.html', {'form': form})
```