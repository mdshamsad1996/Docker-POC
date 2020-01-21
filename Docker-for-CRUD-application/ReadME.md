#### Docker for CRUD application using flask and MySql
Steps to running docker

```
Run: docker-compose up
```
After executing, we will have two containers on our host _my-flask-app_ and *mysql-container* .
For running web application open the brwoser and goto *ec2-ip-address:8081/<entrypoint>*
To destroy the containers, execute:
```
docker-compose down --rmi all
```
Special Note:

app.config['MYSQL_HOST'] = ~~'localhost'~~ ['it should be our database conatiner name']

*Getting Error while  accesing webapplication*

```
MySQLdb._exceptions.OperationalError: (1045, 'Plugin caching_sha2_password could not be loaded: /usr//usr/lib/x86_64-linux-gnu/mariadb19/plugin/caching_sha2_password.so: cannot open shared object file: No such file or directory')
```

Resolution of above error
```
docker exec -it CONTAINER_ID bash
then log into mysql as root

mysql --user=root --password
Enter the password for root (Default is 'root') Finally Run:

ALTER USER 'username' IDENTIFIED WITH mysql_native_password BY 'password';