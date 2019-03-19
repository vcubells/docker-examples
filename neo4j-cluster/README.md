# Ejemplo de un *Causal Cluster* en Neo4j

En este ejemplo se muestra como iniciar un *Causal Cluster* de [Neo4j](https://neo4j.com/).


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Descargue el proyecto y genere los recursos necesarios

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.
3. Cree una red de tipo bridge en Docker

`docker network create cluster`

*Opcional*: Instale los [algoritmos](https://neo4j.com/docs/graph-algorithms/current/)

4. Cree una caroeta 

`mkdir -p $HOME/neo4j/plugins`

5. Siga las instrucciones que aparecen en el [repositorio de GitHub](https://github.com/neo4j-contrib/neo4j-graph-algorithms).


## 3. Iniciar un clúster

1. Cree tres contenedores para los nodos del clúster

```bash
docker run --name=core1 --detach --network=cluster \
    --publish=7474:7474 --publish=7473:7473 --publish=7687:7687 \
    --env=NEO4J_dbms_mode=CORE \
    --env=NEO4J_causal__clustering_expected__core__cluster__size=3 \
    --env=NEO4J_causal__clustering_initial__discovery__members=core1:5000,core2:5000,core3:5000 \
    --env=NEO4J_ACCEPT_LICENSE_AGREEMENT=yes \
    --volume=$HOME/neo4j/data1:/data --volume=$HOME/neo4j/plugins:/plugins \
    --env=NEO4J_AUTH=none \
    --env=NEO4J_dbms_security_procedures_unrestricted=algo.\* \
    neo4j:3.5-enterprise
```
```bash
docker run --name=core2 --detach --network=cluster \
    --publish=8474:7474 --publish=8473:7473 --publish=8687:7687 \
    --env=NEO4J_dbms_mode=CORE \
    --env=NEO4J_causal__clustering_expected__core__cluster__size=3 \
    --env=NEO4J_causal__clustering_initial__discovery__members=core1:5000,core2:5000,core3:5000 \
    --env=NEO4J_ACCEPT_LICENSE_AGREEMENT=yes \
    --volume=$HOME/neo4j/data2:/data --volume=$HOME/neo4j/plugins:/plugins \
    --env=NEO4J_AUTH=none \
    --env=NEO4J_dbms_security_procedures_unrestricted=algo.\* \
    neo4j:3.5-enterprise
```
```bash
docker run --name=core3 --detach --network=cluster \
    --publish=9474:7474 --publish=9473:7473 --publish=9687:7687 \
    --env=NEO4J_dbms_mode=CORE \
    --env=NEO4J_causal__clustering_expected__core__cluster__size=3 \
    --env=NEO4J_causal__clustering_initial__discovery__members=core1:5000,core2:5000,core3:5000 \
    --env=NEO4J_ACCEPT_LICENSE_AGREEMENT=yes \
    --volume=$HOME/neo4j/data3:/data --volume=$HOME/neo4j/plugins:/plugins \
    --env=NEO4J_AUTH=none \
    --env=NEO4J_dbms_security_procedures_unrestricted=algo.\* \
    neo4j:3.5-enterprise
```

2. Conéctese a un nodo del clúster

`docker exec -it core1 cypher-shell`

3. Compruebe el estado del clúster

`CALL dbms.cluster.overview()`


## 4. Adicionar otros tipos de nodos

1. Adicione una réplica de lectura al clúster

```bash
docker run --name=read_replica1 --detach --network=cluster \
    --publish=10474:7474 --publish=10473:7473 --publish=10687:7687 \
    --env=NEO4J_dbms_mode=READ_REPLICA \
    --env=NEO4J_causal__clustering_initial__discovery__members=core1:5000,core2:5000,core3:5000 \
    --env=NEO4J_ACCEPT_LICENSE_AGREEMENT=yes \
    --volume=$HOME/neo4j/data4:/data --volume=$HOME/neo4j/plugins:/plugins \
    --env=NEO4J_AUTH=none \
    --env=NEO4J_dbms_security_procedures_unrestricted=algo.\* \
    neo4j:3.5-enterprise
```

2. Conéctese a un nodo del clúster

`docker exec -it core1 cypher-shell`

3. Compruebe el estado del clúster

`CALL dbms.cluster.overview()`


## 5. Terminar el clúster y eliminar los contenedores

1. Detenga los contenedores:

`docker stop $(docker ps -aq)`

2. Elimine los contenedores:

`docker rm $(docker ps -aq)`


## 6. Recursos

Para aprender sobre Neo4j, favor de referirse a la documentación oficial disponible en [Neo4j Documentation](https://neo4j.com/docs/), al [Developer Portal](https://neo4j.com/developer/) o a los cursos disponibles en [Graph Academy](https://neo4j.com/graph-academy/).

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).
