#### Docker for simple flask hello world application
Steps to running docker

```
Run: docker-compose up
```
After executing, we will have one containers on our host *simple-flask-app*  .
For running web application open the brwoser and goto *ec2-ip-address:8081/<entrypoint>*
To destroy the containers, execute:
```
docker-compose down --rmi all
```
