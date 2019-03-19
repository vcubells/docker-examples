# Ejemplo de una aplicación de Flask ejecutándose en un contenedor Docker

En este ejemplo se muestra como iniciar una aplicación de [Flask API](https://www.flaskapi.org/) en un contenedor [Docker](https://www.docker.com/community-edition), a partir de la generación de una imagen propia, utilizando el comando `docker build `. La aplicación se conecta a una una base de datos de [MongoDB](https://www.mongodb.com/).

## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:
- [Dockerfile](Dockerfile): Archivo de configuración con la especificación necesaria para compilar y generar una imagen personalizada del contenedor.
- [.dockerignore](dockerignore): Archivo que contiene los patrones de nombres de archivos y carpetas que se excluirán al realizar la compilación de la imagen y no serán copiados a la misma.
- [requirements.txt](requirements.txt): Archivo de dependencias.
- [main.py](main.py): Código fuente de la aplicación.


## 3. Instrucciones de uso

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Compile la imagen personalizada de la aplicación:

`docker build -t flask-mongo .`

4. Verifique que la imagen fue creada correctamente y que se encuentra en el repositorio local de imágenes:

`docker images | grep flask-mongo`

5. Cree una red de tipo bridge en docker

`docker network create mynet`

6. Inicie un contenedor con MongoDB:

`docker run --name mongo-server -d --net mynet mongo`

7. Inicie un contenedor con la aplicación, a partir de la imagen generada:

`docker run --name app -p 5000:5000 -d --net mynet flask-mongo`
 
8. Verifique que el contendor se encuentra en ejecución:

`docker ps`

9. Acceda a la interfaz web de la aplicación en un browser en la URL:

[http://localhost:5000](http://localhost:5000)

10. Detenga los contenedores:

`docker stop app`

`docker stop mongo-server`

11. Elimine los contenedores:

`docker rm app`

`docker rm mongo-server`

15. Elimine la imagen en caso de no requerirla:

`docker rmi flask-mongo`


## 4. Recursos

Para aprender a desarrollar una API con Flask API, favor de referirse a la documentación oficial disponible en [Flask API](https://www.flaskapi.org/).  

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).

Para aprender como definir un archivo `Dockerfile`, favor de referirse a la documentación oficial disponible en [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

Para aprender como definir un archivo `.dockerignore`, favor de referirse a la documentación oficial disponible en [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#dockerignore-file).