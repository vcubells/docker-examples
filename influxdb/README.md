# Ejemplo de InfluxDB y Grafana

En este ejemplo se muestra como iniciar [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/) en un contenedor, cargar un dataset de ejemplo y generar un dashboard con [Grafana](https://grafana.com/).


## 1. Pre-requisitos

* Tener instalado `docker`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Descargue el proyecto y genere los recursos necesarios

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto.


## 3. Iniciar un contenedor y cargar el dataset

1. Inicie un contenedor con InfluxDB

`docker run --name influxdb -d -v $PWD/influxdb:/var/lib/influxdb influxdb`

2. Descargue el dataset de ejemplo

`curl https://s3.amazonaws.com/noaa.water-database/NOAA_data.txt -o data.txt`

3. Copie el dataset al contenedor

`docker cp data.txt influxdb:/`

4. Conéctese al bash dlos contenedores

`docker exec -it influxdb bash`

5. Importe el dataset en InfluxDB

`influx -import -path=data.txt -precision=s`

## 4. Ejecutar varias consultas

1. Conéctese al shell de InfluxDB

`influx`

2. Ejecute las siguientes sentencias

```sql 
USE NOAA_water_database

SHOW measurements

SHOW SERIES

SHOW TAG KEYS

SHOW TAG VALUES WITH KEY = "randtag"

SHOW FIELD KEYS

SELECT * FROM "h2o_feet" LIMIT 10

SELECT "level description","location","water_level" FROM "h2o_feet" LIMIT 10

SELECT *::field FROM "h2o_feet"

SELECT ("water_level" * 2) + 4, "water_level" from "h2o_feet" LIMIT 10

SELECT * FROM "h2o_feet","h2o_pH" LIMIT 10

SELECT COUNT("water_level") FROM h2o_feet

SELECT * FROM "h2o_feet" WHERE time > now() - 7d

SELECT * FROM "h2o_feet" WHERE "water_level" > 8

SELECT MEAN("water_level") FROM "h2o_feet" GROUP BY "location"

SELECT COUNT("water_level") FROM "h2o_feet" WHERE "location"='coyote_creek' AND time >= '2015-08-18T00:00:00Z' AND time <= '2015-08-18T00:30:00Z' GROUP BY time(12m)

SELECT "water_level" FROM "h2o_feet" WHERE "location" = 'santa_monica' ORDER BY time DESC
```

## 5. Visualizar los datos con Grafana

1. Inicie un contenedor con Grafana

`docker run --name grafana -d -p 3000:3000  -v $PWD/grafana:/var/lib/grafana grafana/grafana`

2. Conéctese a Grafana

`http://localhost:3000`

3. Acceda con usuario `admin` y contraseña `admin`


## 6. Detener y eliminar los contenedores

1. Detenga los contenedores:

`docker stop $(docker ps -aq)`

2. Elimine los contenedores:

`docker rm $(docker ps -aq)`


## 7. Recursos

Para aprender sobre [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/), favor de referirse a la documentación oficial disponible en [Influxdata Docs](https://www.influxdata.com/time-series-platform/influxdb/).

Para aprender sobre [Grafana](https://grafana.com/), favor de referirse a la documentación oficial disponible en [Grafana Documentation](http://docs.grafana.org/).

Para aprender a trabajar con la línea de comandos de `docker`, favor de referirse a la documentación oficial disponible en [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli/).
