# Ejemplo de un MongoDB Sharding Cluster

En este ejemplo se muestra como iniciar un **Sharding Cluster** de [MongoDB](https://www.mongodb.com/).


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Descargue el proyecto y genere los recursos necesarios

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Cree una red de tipo bridge en Docker

`docker network create mongo-sh`

## 3. Iniciar un ReplicaSet para los nodos de configuración

1. Cree tres contenedores para los nodos del ReplicaSet de configuración

`docker run --name mongo-config1 -d --net mongo-sh mongo --replSet "rsConfig" --configsvr`

`docker run --name mongo-config2 -d --net mongo-sh mongo --replSet "rsConfig" --configsvr`

`docker run --name mongo-config3 -d --net mongo-sh mongo --replSet "rsConfig" --configsvr`

2. Iniciar una terminal en uno de los nodos

`docker exec -it mongo-config1 bash`

3. Conéctese a uno de los nodos 

`mongo --host mongo-config1 --port 27019`

4. Inicialice el ReplicaSet de configuración

```js
config = {
      "_id" : "rsConfig",
      "configsvr": true,
      "members" : [
          {
              "_id" : 0,
              "host" : "mongo-config1:27019"
          },
          {
              "_id" : 1,
              "host" : "mongo-config2:27019"
          },
          {
              "_id" : 2,
              "host" : "mongo-config3:27019"
          }
      ]
  }

rs.initiate(config)
```

5. Desconéctse del cliente de `mongo`

`exit` 

6. Desconéctese del contenedor

`exit`


## 4. Iniciar un ReplicaSet para el Shard 1

1. Cree tres contenedores para los nodos del ReplicaSet del shard 1

`docker run --name mongo-shard11 -d --net mongo-sh mongo --replSet "rsShard1" --shardsvr`

`docker run --name mongo-shard12 -d --net mongo-sh mongo --replSet "rsShard1" --shardsvr`

`docker run --name mongo-shard13 -d --net mongo-sh mongo --replSet "rsShard1" --shardsvr`

2. Iniciar una terminal en uno de los nodos

`docker exec -it mongo-shard11 bash`

3. Conéctese a uno de los nodos 

`mongo --host mongo-shard11 --port 27018`

4. Inicialice el ReplicaSet del Shard 1

```js
config = {
      "_id" : "rsShard1",
      "members" : [
          {
              "_id" : 0,
              "host" : "mongo-shard11:27018"
          },
          {
              "_id" : 1,
              "host" : "mongo-shard12:27018"
          },
          {
              "_id" : 2,
              "host" : "mongo-shard13:27018"
          }
      ]
  }

rs.initiate(config)
```

5. Desconéctse del cliente de `mongo`

`exit` 

6. Desconéctese del contenedor

`exit`


## 5. Iniciar un ReplicaSet para el Shard 2

1. Cree tres contenedores para los nodos del ReplicaSet del shard 2

`docker run --name mongo-shard21 -d --net mongo-sh mongo --replSet "rsShard2" --shardsvr`

`docker run --name mongo-shard22 -d --net mongo-sh mongo --replSet "rsShard2" --shardsvr`

`docker run --name mongo-shard23 -d --net mongo-sh mongo --replSet "rsShard2" --shardsvr`

2. Iniciar una terminal en uno de los nodos

`docker exec -it mongo-shard21 bash`

3. Conéctese a uno de los nodos 

`mongo --host mongo-shard21 --port 27018`

4. Inicialice el ReplicaSet del Shard 1

```js
config = {
      "_id" : "rsShard2",
      "members" : [
          {
              "_id" : 0,
              "host" : "mongo-shard21:27018"
          },
          {
              "_id" : 1,
              "host" : "mongo-shard22:27018"
          },
          {
              "_id" : 2,
              "host" : "mongo-shard23:27018"
          }
      ]
  }

rs.initiate(config)
```

5. Desconéctse del cliente de `mongo`

`exit` 

6. Desconéctese del contenedor

`exit`


## 6. Iniciar un Router

1. Cree un contenedor para el router

`docker run  --name mongo-router -d --net mongo-sh mongo  mongos --configdb rsConfig/mongo-config1:27019,mongo-config2:27019,mongo-config3:27019`

2. Conéctese al router

`docker exec -it mongo-router mongo`

3. Adicione los Shards al clúster

`sh.addShard( "rsShard1/mongo-shard11:27018")`

`sh.addShard( "rsShard2/mongo-shard21:27018")`

4. Habilite el *sharding* para una base de datos

`sh.enableSharding("mydbname")`

5. Habilite el *sharding* en una colección

Por rango: `sh.shardCollection("mydbname.mycollection",  { "mykey" : 1 } )`

o

Por hash: `sh.shardCollection("shdb.data", { "mykey" : "hashed" } )`


## 7. Monitorear el estado del clúster

1. Ver el estado del *sharding* cluster
```js
use mydbname
sh.status()
db.printShardingStatus() 
```

2. Ver las bases de datos con *sharding*

```js
use config
db.databases.find( { "partitioned": true } )
````

3. Ver la lista de *shards*

```js
use admin
db.adminCommand( { listShards : 1 } )
```

## 8. Insertar datos en el cluster

1. Inserte un conjunto de registros 
```js
use mydbname
var bulk = db.mycollection.initializeUnorderedBulkOp();
people = ["Marc", "Bill", "George", "Eliot", "Matt", "Trey", "Tracy", "Greg", "Steve", "Kristina", "Katie", "Jeff"];
for(var i=0; i<1000000; i++){
   user_id = i;
   name = people[Math.floor(Math.random()*people.length)];
   number = Math.floor(Math.random()*10001);
   bulk.insert( { "user_id":user_id, "name":name, "number":number });
}
bulk.execute();
```

2. Divida los datos entre *chunks*

`sh.splitFind( "mydbname.mycollection", { "number": 4000 } )`

* En caso de insertar los datos antes de habilitar el *sharding*, ejecute lo siguiente

```js
sh.enableSharding( "mydbname" )
db.data.createIndex( { number : 1 } )
sh.shardCollection( "mydbname.mycollection", { "number" : 1 } )
```

## 9. Eliminar un *shard*

```js
use admin
db.adminCommand( { removeShard: "<shard_name>" } )
```

## 10. Terminar el clúster y eliminar los contenedores

1. Detenga los contenedores:

`docker stop $(docker ps -aq)`

2. Elimine los contenedores:

`docker rm $(docker ps -aq)`


## 11. Recursos

Para aprender sobre MongoDB, favor de referirse a la documentación oficial disponible en [MongoDB Manual](https://docs.mongodb.com/manual/) o a los cursos disponibles en [MongoDB University](https://university.mongodb.com/).

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).