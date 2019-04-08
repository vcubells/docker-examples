# Ejemplo de inciar Cassandra en un contenedor de Docker

En este ejemplo se muestra como iniciar [Cassandra](http://cassandra.apache.org/) en un contenedor.


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Descargue el proyecto y genere los recursos necesarios

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Cree una red para Cassandra

`docker network create cassandra`


## 3. Iniciar un contenedor y crear la base de datos

### 3.1 Utilizando la imagen de Cassandra

1. Cree un contenedor

`docker run --name cassandra-db -d --network cassandra -e CASSANDRA_SEEDS=cassandra-db cassandra` 

2. Conéctese al contenedor

`docker exec -it --rm cassandra-db bash`

3. Conéctese a la consola de Cassandra

`cqlsh`

### 3.2 Utilizando DataStax

1. Descargue la imagen de DataStax

`docker pull datastax/dse-server:latest`

2. Descargue la imagen de DataStax Studio

`docker pull datastax/dse-studio:latest`

3. Ejecute un contenedor con DataStax

`docker run --name datastax-server -e DS_LICENSE=accept --memory 4g -d --net cassandra datastax/dse-server -g -s -k`

4. Ejecute un contenedor con DataStax Studio

`docker run --name studio -e DS_LICENSE=accept  -p 9091:9091 --memory 1g  -d --net cassandra datastax/dse-studio`

5. Conéctese a DataStax Studio

`http://localhost:9091`

6. Conéctese al contenedor

`docker exec -it --rm datastax-server bash`

7. Revise el status del contenedor 

`nodetool status`

8. Conéctese a la consola de Cassandra

`cqlsh`


## 4. Detener y eliminar los contenedores

1. Detenga los contenedores:

`docker stop $(docker ps -aq)`

2. Elimine los contenedores:

`docker rm $(docker ps -aq)`


## 5. Recursos

Para aprender sobre [Cassandra](http://cassandra.apache.org/), favor de referirse a la documentación oficial disponible en [Apache Cassandra Documentation](http://cassandra.apache.org/doc/latest/).

Para aprender sobre [DataStax](https://www.datastax.com/), favor de referirse a la documentación oficial disponible en [DataStax Docs](https://docs.datastax.com/en/landing_page/doc/landing_page/current.html) o a los cursos disponibles en [DataStax Academy](https://academy.datastax.com/).

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).
