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
    checkBox = models.BooleanField()

    def __str__(self):
        return self.title
```