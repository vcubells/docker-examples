# Ejemplo de Grafana + InfluxDB utilizando Docker Compose

En este ejemplo se muestra como iniciar una aplicación compuesta por dos microservicios ([Grafana](https://grafana.com/) e [InfluxDB](https://www.influxdata.com/time-series-platform/)), utilizando `docker-compose`. Cada servicio se ejecuta en su propio contenedor, y estos, se encuentran enlazados entre sí. 

## 1. Pre-requisitos

* Tener instalado `docker` y `docker-compose`. Mas información se encuentra disponible en [Docker](https://www.docker.com/community-edition).
* Acceso a Internet.


## 2. Estructura del proyecto

A continuación se describen los archivos y carpetas que forman parte del proyecto, así como la función que juega cada uno de ellos:
- [grafana](grafana): Carpeta donde se almacenará toda la información persistente de Grafana, como por ejemplo, los *plugins* que se instalan durante la ejecución del contenedor y que aparecen especificados en el archivo [env.grafana](env.grafana).
- [influxdb](influxdb): Carpeta donde se almacenará toda la información persistente de InfluxDB, como por ejemplo, las bases de datos.
- [env.grafana](env.grafana): Archivo de configuración donde se definen las variables de ambiente que utilizará Grafana durante su ejecución. Aquí es donde se definen los *plugins* que se instalarán inicialmente.
- [env.influxdb](env.influxdb): Archivo de configuración donde se definen las variables de ambiente que utilizará InfluxDB durante su ejecución.
- [docker-compose.yml](docker-compose.yml): Archivo de configuración donde se definen los servicios (Grafana e InfluxDB) a ejecutar dentro de los contendores.


## 3. Instrucciones de uso

1. Descargue el repositorio a una carpeta de su computadora utilizando el comando `git clone`.
2. Cámbiese a la carpeta del proyecto y cree las carpetas necesarias:

`mkdir grafana`
`mkdir influxdb`

3. Ejecute el comando:

`docker-compose up -d`
 
4. Acceda a la interfaz web de Grafana en un browser en la URL:

[http://localhost:3000](http://localhost:3000)

5. Detenga la ejecución de los contenedores:

`docker-compose stop`

6. Inicie la ejecución de los contenedores:

`docker-compose start`

7. En caso de desearlo, puede eliminar tanto los contenedores creados como las imágenes:

`docker-compose down --rmi all`

## 4. Recursos

Para aprender a generar diferentes tipos de tableros (*dashboards*) en Grafana, favor de referirse a la documentación oficial disponible en [Grafana Labs](http://docs.grafana.org/).

Para aprender a trabajar con los datos en una base de datos de InfluxDB, favor de referirse a la documentación oficial disponible en [influxdata](https://docs.influxdata.com/influxdb/)

Para aprender a trabajar con el comando `docker-compose`,  favor de referirse a la documentación oficial disponible en [docker-compose CLI](https://docs.docker.com/compose/reference/overview/).