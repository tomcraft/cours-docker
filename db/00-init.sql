CREATE USER 'app'@'%' IDENTIFIED BY 'appPass';
GRANT ALL PRIVILEGES ON `sakila` . * TO 'app'@'%';
FLUSH PRIVILEGES;