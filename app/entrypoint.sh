#!/bin/bash

echo waiting for database on ${MYSQL_HOST}:${MYSQL_PORT}

while ! nc -z ${MYSQL_HOST} ${MYSQL_PORT}
do
  sleep 0.5
done

echo database found

if [[ -z "${SAKILA_DEBUG}" ]]; then
  UVICORN_FLAGS="--reload"
fi

uvicorn main:app ${UVICORN_FLAGS} --host 0.0.0.0 --port ${PORT}
