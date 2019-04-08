# Ejemplo de IBM DB2 Express-C

En este ejemplo se muestra como iniciar IBM DB2 Express-C en un contenedor.


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Descargue el proyecto y genere los recursos necesarios

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.


## 3. Iniciar un contenedor y crear la base de datos

1. Cree un contenedor

`docker run --name db2 -d -p 50000:50000 -e DB2INST1_PASSWORD=db2inst1-pwd -e LICENSE=accept ibmcom/db2express-c:latest` 

2. Conéctese al contenedor

`docker exec -it db2 bash`

3. Cámbiese al usuario administrador de DB2

`su - db2inst1`

4. Inicie el servidor de DB2

`db2start`

5. Conéctese a la consola de DB2

`db2`


## 4. Detener y eliminar el contenedor

1. Detenga el contenedor:

`docker stop db2`

2. Elimine el contenedor:

`docker rm db2`



## 7. Recursos

Para aprender sobre IBM DB2 Express-C, favor de referirse a la documentación oficial disponible en [IBM](https://www.ibm.com/products/software) o a los materiales disponibles en [IBM Community](https://community.ibm.com/community/user/hybriddatamanagement/home).

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).
