FROM python:3.9

WORKDIR /usr/src/app

RUN apt update &&\
  apt install -y netcat &&\
  rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
ENV PORT=8000
ENV MYSQL_HOST="" MYSQL_PORT="3306" MYSQL_USER="" MYSQL_PASSWORD="" MYSQL_DB=""

ENTRYPOINT [ "./entrypoint.sh" ]