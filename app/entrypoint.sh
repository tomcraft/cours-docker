#!/bin/bash

echo waiting for database on ${MYSQL_HOST}:${MYSQL_PORT}

while ! nc -z ${MYSQL_HOST} ${MYSQL_PORT}
do
  sleep 0.5
done

echo database found

if [[ -z "${SAKILA_DEBUG}" ]]; then
  uvicorn main:app --reload --port ${PORT}
else
  uvicorn main:app --port ${PORT}
fi
