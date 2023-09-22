# Machine Learning API

The purpose of this code is to illustrate the use of FASTAPI 
for machine learning inference. 


# SETUP 
We first need to build the docker image
```
docker build -t fastapi .
docker run -d --cpus="1" --memory=2000m --name test -p 80:80 fastapi
```
# AUTHOR 
Bryan Piguave Llano
