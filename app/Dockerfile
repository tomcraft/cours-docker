FROM python:3.9

WORKDIR /usr/src/app

RUN apt update &&\
  apt install -y netcat &&\
  rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
ENV MYSQL_HOST=
ENV MYSQL_PORT="3306"
ENV MYSQL_USER=
ENV MYSQL_PASSWORD=
ENV MYSQL_DB=

ENTRYPOINT [ "./entrypoint.sh" ]