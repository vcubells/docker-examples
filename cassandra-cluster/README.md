# Ejemplo de iniciar un clúster de Cassandra en contenedores de Docker

En este ejemplo se muestra como iniciar un clúster de [Cassandra](http://cassandra.apache.org/) en contenedores.


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Descargue el proyecto y genere los recursos necesarios

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Cree una red para Cassandra

`docker network create cassandra`

## 3. Iniciar un clúster

1. Cree el primer nodo del clúster

`docker run --name node1  -p 9042:9042 --network cassandra -e CASSANDRA_CLUSTER_NAME=cassandra-cluster -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra` 

2. Obtenga la dirección IP del contendore anterior

`docker inspect --format='{{ .NetworkSettings.Networks.cassandra.IPAddress }}' node1`

3. Cree otros nodos del clúster. No olvide sustituir la IP por la obtenido en el paso anterior

`docker run --name node2  --network cassandra -e CASSANDRA_SEEDS="<IP_ADDRESS>" -e CASSANDRA_CLUSTER_NAME=cassandra-cluster -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter1 -d cassandra`

`docker run --name node3  --network cassandra -e CASSANDRA_SEEDS="<IP_ADDRESS>" -e CASSANDRA_CLUSTER_NAME=cassandra-cluster -e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch -e CASSANDRA_DC=datacenter2 -d cassandra`

4. Conéctese al contenedor

`docker exec -it --rm node1 bash`

5. Revise el status del clúster. Deben aparecer los tres nodos distribuidos en dos datacenters 

`nodetool status`

6. Conéctese a la consola de Cassandra

`cqlsh`

7. Crear un KEYSPACE con replicación

```sql 
CREATE KEYSPACE testkeyspace
WITH replication = {
'class' : 'NetworkTopologyStrategy',
'datacenter1' : 1,
'datacenter2' : 1
};
```

8. Cree una tabla

```sql 
CREATE TABLE testkeyspace.mytable (
	id int primary key,
	name text
);
```

9. Desconéctese de la consola de Cassandra

`exit`

10. Revise la distribución de los datos en el clúster

`nodetool status testkeyspace`

11. Deconéctese del shell

`exit`

### Opcional: Conéctese utilizando DataStax Studio

1. Descargue la imagen de DataStax Studio

`docker pull datastax/dse-studio:latest`

2. Ejecute un contenedor con DataStax Studio

`docker run --name studio -e DS_LICENSE=accept  -p 9091:9091 --memory 1g  -d --net cassandra datastax/dse-studio`

3. Conéctese a DataStax Studio

`http://localhost:9091`


## 4. Detener y eliminar los contenedores

1. Detenga los contenedores:

`docker stop $(docker ps -aq)`

2. Elimine los contenedores:

`docker rm $(docker ps -aq)`


## 5. Recursos

Para aprender sobre [Cassandra](http://cassandra.apache.org/), favor de referirse a la documentación oficial disponible en [Apache Cassandra Documentation](http://cassandra.apache.org/doc/latest/).

Para aprender sobre [DataStax](https://www.datastax.com/), favor de referirse a la documentación oficial disponible en [DataStax Docs](https://docs.datastax.com/en/landing_page/doc/landing_page/current.html) o a los cursos disponibles en [DataStax Academy](https://academy.datastax.com/).

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).
