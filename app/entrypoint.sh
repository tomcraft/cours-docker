#!/bin/bash

echo waiting for database on ${MYSQL_HOST}:${MYSQL_PORT}

while ! nc -z ${MYSQL_HOST} ${MYSQL_PORT}
do
  sleep 0.5
done

echo database found

python ./main.py