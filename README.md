
# Sakila-CRUD

Sakila-CRUD est un projet backend python permettant des interactions simples avec [le schema Sakila](https://dev.mysql.com/doc/sakila/en/sakila-introduction.html) développé par MySQL.
## Prérequis

- Docker
- Docker-Compose

## Intallation

Clonner le projet

```bash
  git clone https://github.com/tomcraft/cours-docker sakila-crud
```

Entrer dans le dossier du projet

```bash
  cd sakila-crud
```

Démarrer l'application

```bash
  docker-compose up -d
```

## Documentation

- Swagger (OpenAPI): http://localhost:8080/docs

## Log de build
```
thomas@MacBook-Pro-de-Thomas docker % docker-compose build      

db uses an image, skipping
Building app
[+] Building 1.8s (12/12) FINISHED                                                                                                         
 => [internal] load build definition from Dockerfile                                                                                  0.0s
 => => transferring dockerfile: 286B                                                                                                  0.0s
 => [internal] load .dockerignore                                                                                                     0.0s
 => => transferring context: 2B                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                                         1.6s
 => [auth] library/python:pull token for registry-1.docker.io                                                                         0.0s
 => [1/6] FROM docker.io/library/python:3.9@sha256:61cb1ea441cba629934a49a384dcb501154746fa0139f601f4d733f7b956c359                   0.0s
 => [internal] load build context                                                                                                     0.0s
 => => transferring context: 808B                                                                                                     0.0s
 => CACHED [2/6] WORKDIR /usr/src/app                                                                                                 0.0s
 => CACHED [3/6] RUN apt update &&  apt install -y netcat &&  rm -rf /var/lib/apt/lists/*                                             0.0s
 => CACHED [4/6] COPY requirements.txt ./                                                                                             0.0s
 => CACHED [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                   0.0s
 => CACHED [6/6] COPY . .                                                                                                             0.0s
 => exporting to image                                                                                                                0.0s
 => => exporting layers                                                                                                               0.0s
 => => writing image sha256:8dc34d13b00c3e0568a6bbd93ffb1236f4a5fe207059c5381a634f04a8412132                                          0.0s
 => => naming to docker.io/library/docker_app                                                                                         0.0s
 ```