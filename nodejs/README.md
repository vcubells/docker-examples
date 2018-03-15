# Ejemplo de una aplicación Node.js ejecutándose en un contenedor Docker

En este ejemplo se muestra como iniciar una aplicación de [Node.js](https://nodejs.org/en/) en un contenedor [Docker](https://www.docker.com/community-edition), a partir de la generación de una imagen propia, utilizando el comando `docker build `. 

## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:
- [Dockerfile](Dockerfile): Archivo de configuración con la especificación necesaria para compilar y generar una imagen personalizada del contenedor.
- [.dockerignore](dockerignore): Archivo que contiene los patrones de nombres de archivos y carpetas que se excluirán al realizar la compilación de la imagen y no serán copiados a la misma.
- [index.js](index.js): Código fuente de la aplicación Node.js.
- [package.json](package.json): Archivo de configuración de la aplicación Node.js.


## 3. Instrucciones de uso

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Compile la imagen personalizada de la aplicación:

`docker build -t nodejs:webinar .`

4. Verifique que la imagen fue creada correctamente y que se encuentra en el repositorio local de imágenes:

`docker images | grep nodejs:webinar`

5. Revise la información de la imagen creada

`docker inspect nodejs:webinar`

6. Inicie un contenedor a partir de la imagen generada:

`docker run --name app-web -p 80:80 -d nodejs:webinar`
 
7. Verifique que el contendor se encuentra en ejecución:

`docker ps`

8. Acceda a la interfaz web de la aplicación en un browser en la URL:

[http://localhost](http://localhost)

9. Detenga el contenedor:

`docker stop app-web`

10. Vuelva a iniciar el contendor:

`docker start app-web`

11. Revise los logs de su aplicación para verificar si hay algún problema:

`docker logs app-web`

12. Revise la información de su contenedor:

`docker info app-web`

13. Detenga el contenedor:

`docker stop app-web`

14. Elimine el contenedor si no lo va a utilizar más:

`docker rm app-web`

15. Elimine la imagen en caso de no requerirla:

`docker rmi nodejs:webinar`


## 4. Recursos

Para aprender a desarrollar una aplicación web con Node.js, favor de referirse a la documentación oficial disponible en [Node.js Docs](https://nodejs.org/en/docs/) o a los diferentes cursos disponibles en plataformas como [Cousera](https://www.coursera.org/courses?languages=en&query=node.js), [Udemy](https://www.udemy.com/courses/search/?q=node.js&src=ukw), entre otros.  

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).

Para aprender como definir un archivo `Dockerfile`, favor de referirse a la documentación oficial disponible en [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

Para aprender como definir un archivo `.dockerignore`, favor de referirse a la documentación oficial disponible en [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#dockerignore-file).