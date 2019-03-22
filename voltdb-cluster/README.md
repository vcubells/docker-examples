# Ejemplo de un clúster

En este ejemplo se muestra como iniciar un clúster de [VoltDB](https://www.voltdb.com/).


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Descargue el proyecto y genere los recursos necesarios

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Cree una red de tipo bridge en Docker

`docker network create voltdb-cluster`


## 3. Iniciar un clúster

1. Cree tres contenedores para los nodos del clúster

`docker run --name node1 --hostname node1 -d -P --net voltdb-cluster -e HOST_COUNT=3 -e HOSTS=node1 voltdb/voltdb-community`

`docker run --name node2 --hostname node2 -d -P --net voltdb-cluster -e HOST_COUNT=3 -e HOSTS=node1 voltdb/voltdb-community`

`docker run --name node3 --hostname node3 -d -P --net voltdb-cluster -e HOST_COUNT=3 -e HOSTS=node1 voltdb/voltdb-community`

2. Conéctese a un nodo del clúster

`docker exec -it node1 sqlcmd`

3. Conéctese a la consola 

`sqlcmd`



## 4. Terminar el clúster y eliminar los contenedores

1. Detenga los contenedores:

`docker stop $(docker ps -aq)`

2. Elimine los contenedores:

`docker rm $(docker ps -aq)`



## 7. Recursos

Para aprender sobre VoltDB, favor de referirse a la documentación oficial disponible en [VoltDB Documentation](https://docs.voltdb.com/) o a los cursos disponibles en [VoltDB University](https://university.voltdb.com/).

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).
