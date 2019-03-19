# Ejemplo de un MongoDB ReplicaSet

En este ejemplo se muestra como iniciar un ReplicaSet de [MongoDB](https://www.mongodb.com/).


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Descargue el proyecto y genere los recursos necesarios

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Cree una red de tipo bridge en Docker

`docker network create mongo-rs`


## 3. Iniciar un ReplicaSet

1. Cree tres contenedores para los nodos del ReplicaSet

`docker run --name mongo-node1 -d --net mongo-rs mongo --replSet "rs0"`

`docker run --name mongo-node2 -d --net mongo-rs mongo --replSet "rs0"`

`docker run --name mongo-node3 -d --net mongo-rs mongo --replSet "rs0"`

2. Conéctese a uno de los nodos

`docker exec -it mongo-node1 mongo`

3. Inicialice el ReplicaSet

```json
config = {
      "_id" : "rs0",
      "members" : [
          {
              "_id" : 0,
              "host" : "mongo-node1:27017"
          },
          {
              "_id" : 1,
              "host" : "mongo-node2:27017"
          },
          {
              "_id" : 2,
              "host" : "mongo-node3:27017"
          }
      ]
  }

  rs.initiate(config)
  ```

4. Compruebe el estado del ReplicaSet

`rs.status()`

5. Determine si el nodo en el cual está posicionado es el `master`:

`rs.isMaster()`

6. Para habilitar los nodos secundarios para lectura, conéctese a cada nodo y ejecute el comando:

`rs.slaveOk()`


## 4. Adicionar otros tipos de nodos

### 4.1 Adicionar un nodo secundario que no puede votar

1. Cree un nuevo contenedor

`docker run --name mongo-node4 -d --net mongo-rs mongo --replSet "rs0"`

2. Conéctese a uno de los nodos del ReplicaSet

`docker exec -it mongo-node1 mongo`

3. Adicione el nuevo nodo al ReplicaSet

`rs.add( { host: "mongo-node4:27017", priority: 0, votes: 0 } )`

### 4.2 Adicionar un árbitro

1. Cree un nuevo contenedor

`docker run --name mongo-arb -d --net mongo-rs mongo --replSet "rs0"`

2. Conéctese a uno de los nodos del ReplicaSet

`docker exec -it mongo-node1 mongo`

3. Adicione el nuevo nodo al ReplicaSet

`rs.addArb("mongo-arb:27017")`


## 5. Reconfigurar los nodos

1. Conéctese a uno de los nodos del ReplicaSet

`docker exec -it mongo-node1 mongo`

2. Obtenga la configuración actual

`cfg = rs.conf();`

3. Modifique la configuración

`cfg.members[1].priority = 2;`

4. Reconfigure el ReplicaSet

`rs.reconfig(cfg);`


## 6. Eliminar nodos del ReplicaSet

1. Conéctese al nodo del ReplicaSet que desea eliminar

`docker exec -it mongo-node3 mongo`

2. Detenga el servicio

`db.shutdownServer()`

3. Elimine el nodo

`rs.remove("mongo-node3")`

## 7. Forzar una votación

1. Conéctese al nodo primario del ReplicaSet

`docker exec -it mongo-node1 mongo`

2. Fuerce que deje de ser el primario

`rs.stepDown()`


## 8. Obtener información del Oplog

1. Conéctese al nodo primario del ReplicaSet

`docker exec -it mongo-node1 mongo`

2. Ejecute los comandos siguientes

`rs.printReplicationInfo()`
`rs.printSlaveReplicationInfo()`


## 9. Terminar el ReplicaSet y eliminar los contenedores

1. Detenga los contenedores:

`docker stop $(docker ps -aq)`

2. Elimine los contenedores:

`docker rm $(docker ps -aq)`



## 10. Recursos

Para aprender sobre MongoDB, favor de referirse a la documentación oficial disponible en [MongoDB Manual](https://docs.mongodb.com/manual/) o a los cursos disponibles en [MongoDB University](https://university.mongodb.com/).

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).
