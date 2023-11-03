Crear un .gitignore:
    *.pyc
    *~
    __pycache__
    entornoTask
    db.sqlite3
    /static
    .DS_Store

He creado un entorno virtual poniendo: python3 -m venv entornoTask

He iniciado el entorno virtual: source entornoTask/bin/activate

Crear el requeriments.txt y añadir django: Django~=4.2.7
Se puede actualizar asi: pip install --upgrade django por linea de comandos

Luego he instalado lo que habia en requirements.txt: pip install -r requirements.txt 

django-admin startproject mysite . para crear mysite