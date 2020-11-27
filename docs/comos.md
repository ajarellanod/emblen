# Archivo Como's

## Como crear y encender entorno virtual

Seguir paso a paso los siguientes comandos en la cmd de windows.

1. `pip install virtualenv`
2. `virtualenv env`
3. `cd env/scripts`
4. `activate.bat`

---

## Como clonar repositorio e instalar dependencias

Seguir paso a paso los siguientes comandos en la cmd de windows.

Nota: Verificar si es la ruta que se quiere.

1. `git clone https://github.com/ajarellanod/emblen.git`
2. `cd nombre-de-la-carpeta-clonada`
3. `pip install -r requirements.txt`

---

## Como correr el proyecto en desarrollo

Seguir paso a paso los siguientes comandos en la cmd de windows.

Nota: Verificar con el comando `dir` si en la ruta donde estas se encuentra el archivo manage.py.

1. `python manage.py migrate`
2. `python manage.py createsuperuser` - Este comando crea un super usuario que puedes darle el nombre que prefieras.
3. `python manage.py runserver` - La consola creara un servidor en http://127.0.0.1:8000/, si cierras la consola se detendra el servidor.