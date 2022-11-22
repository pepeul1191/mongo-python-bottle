# MongoDB

## Docker

Ver lista de containers deplegados

	$ docker ps

Escribir el código de docker-compose.yml

```yml
version: "3.8"
services:
  mongodb:
    image : mongo
    container_name: mongodb
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - {ruta en disco}:/data/db
    ports:
      - 27019:27017
    restart: unless-stopped
```

db.usuario.insertMany([
  {usuario: 'pepe', constrasenia: '123', accesos: []},
  {usuario: 'sila', constrasenia: '123', accesos: []},
])

Modificar en la línea de la llave 'volumnes' con una ruta en disco donde que quiera almacenar la db.

Arrancar containers en base a lo escrito en .yml

	$ docker compose up

Acceder al bash del container:

	$ docker exec -it <id_container> bash

En el docker:

  $ mongosh

---

Fuentes:

+ https://avbravo-2.gitbook.io/docker/mongodb
+ https://www.bmc.com/blogs/mongodb-docker-container/
+ https://stackoverflow.com/questions/73582703/mongo-command-not-found-on-mongodb-6-0-docker-container
+ https://pymongo.readthedocs.io/en/stable/tutorial.html#making-a-connection-with-mongoclient