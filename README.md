# Como Funciona

El proyecto esta desarrollado en el lenguaje de programacion Python, haciendo uso del framework Django y herramientas adicionales como Bootstrap.

### Como correr el proyecto

Dependiendo que usuario seas los comandos pueden cambiar, asi que presta atencion para que el proyecto funcione correctamente.

> Instalacion

* Descarga el proyecto del repositorio de github:

	```
	git clone ...
	```

* Crea un entorno virtual

	Windows:
    
    ``` 
    py -m venv venv
    ```
    
    Linux/Mac:
    
  	```
    python3 -m venv venv
    ```
    
* Entra al entorno virtual

	Windows:
	
    ```
    .\venv\Scripts\activate
    ```
    
    Linux/Mac:
    ```
    source venv/bin/activate
    ```
   
* Instala los requerimientos
	
    Windows/Linux/Mac:
    ```
    pip install -r requirements.txt
    ```
* Revisa que no haya cambios en las migraciones
	
    Windows:
    ```
    py manage.py makemigrations
    ```
    Linux/Mac:
    ```
    python3 manage.py makemigrations
    ```
* Realiza las migraciones
	
    Windows:
    ```
    py manage.py migrate
    ```
    Linux/Mac:
    ```
    python3 manage.py migrate
    ```
> Crear un super usuario
* Crea un usuario administrador:
	
    Windows
    ```
    py manage.py createsuperuser
    ```
    Linux/Mac:
    ```
    python3 manage.py createsuperuser
    ```
    
> Correr el servidor
* Corre el servidor y prueba al app
	
    Windows:
    ```
    py manage.py runserver
    ```
    Linux/Mac:
    ```
    python3 manage.py runserver
    ```
    
    Ingresa a [localhost:8000/](localhost:8000/) para probar el sistema como usuario 'normal' o ingresa a [localhost:8000/admin/](localhost:8000/admin/) y prueba la app como administrador.
    
### Contribuye al proyecto siendo CONTRIBUTOR

Descarga el proyecto de github a tu computadora, crea una nueva rama con el comando:
```
git checkout -b 'nombre_de_rama'
```
Realiza los cambios que consideres pertinentes, guardalos y antes de hacer un merge asegurate de tener la ultima version del proyecto usando los siguientes comandos:
```
git checkout main
git pull origin main
```
Completa la fusion de las ramas con el comando:
```
git merge 'nombre_de_rama' -m "Un comentario de los cambios"
```
Finalmente envia tus cambios al repositorio usando:
```
git push origin main
```
    
