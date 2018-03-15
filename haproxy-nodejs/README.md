# Ejemplo de HAproxy + Node.js utilizando Docker Compose

En este ejemplo se muestra como iniciar una aplicación compuesta por dos microservicios: [HAProxy](http://www.haproxy.org/) como balanceador y una aplicación en [Node.js](https://nodejs.org/en/). Para lo anterior se utiliza `docker-compose`. Cada servicio se ejecuta en su propio contenedor, y estos, se encuentran enlazados entre sí. 

Esta aplicación puede escalar, incrementando el número de instancias del contenedor correspondiente a la aplicación web, y el balanceador automáticamente detecta cuántos servidores de *backend* se encuentran disponibles y balancea las solicitudes entre ellos.


## 1. Pre-requisitos

* Tener instalado `docker` y `docker-compose`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.
* Tener compilada de manera local una imagen del contenedor de la aplicación Node.js que se encuentra en la carpeta [nodejs](../nodejs) de este repositorio. En caso de querer utilizar una imagen diferente, favor de cambiar la línea `image: nodejs:webinar` en el archivo [docker-compose.yml](docker-compose.yml).


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:
- [docker-compose.yml](docker-compose.yml): Archivo de configuración donde se definen los servicios (HAProxy y la aplicación Node.js) a ejecutar dentro de los contendores.


## 3. Instrucciones de uso

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Ejecute el comando:

`docker-compose up -d --scale web=3`

Si no define un `número de instancias`, en este caso es 3, solamente se inicia un contenedor de cada servicio.

Posteriormente, puede escalar la solución ejecutando el comando:

`docker-compose up --scale web=10`

El nuevo valor del `número de instancias` debe ser igual a la suma de los contenedores en ejecución más el número de nuevos contendores a iniciar. En este ejemplo se tienen 3 servidores web y se quiere scalar la solución con 7 servidores más, lo cual hace un total de 10 servidores de *backend*.

4. Acceda a la interfaz web de la aplicación en un browser en la URL:

[http://localhost](http://localhost)

5. Visualice las estadísticas del comportamiento del balanceador HAProxy accediendo a la URL [http://localhost:81](http://localhost:81) y utilizando las siguientes credenciales de acceso:

**user**: `stats` 
**password**: `stats`

6. Detenga la ejecución de los contenedores:

`docker-compose stop`

7. Inicie la ejecución de los contenedores:

`docker-compose start`

8. En caso de desearlo, puede eliminar tanto los contenedores creados como las imágenes:

`docker-compose down --rmi all`

## 4. Recursos

Para aprender a desarrollar una aplicación web con Node.js, favor de referirse a la documentación oficial disponible en [Node.js Docs](https://nodejs.org/en/docs/) o a los diferentes cursos disponibles en plataformas como [Cousera](https://www.coursera.org/courses?languages=en&query=node.js), [Udemy](https://www.udemy.com/courses/search/?q=node.js&src=ukw), entre otros.  

Para aprender a trabajar con el balanceador HAProxy,  favor de referirse a la documentación oficial disponible en [HAProxy Docs](http://www.haproxy.org/#docs).

Para aprender a trabajar con el comando `docker-compose`,  favor de referirse a la documentación oficial disponible en [docker-compose CLI](https://docs.docker.com/compose/reference/overview/).