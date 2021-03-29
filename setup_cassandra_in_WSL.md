# setup apache cassandra in WSL

step1: install docker

https://www.docker.com/products/docker-desktop 

step2: login to docker

> docker login

step3: pull cassandra docker image

> docker pull cassandra

step3: start your cassandra container

> docker run --name <name_your_container> -p 127.0.0.1:9042:9042 -d cassandra

step4: python driver for cassandra

> pip install cassandra-driver

step5: open your jupyter notebook and start writing your etl pipeline

More about the cassandra docker image [here](https://hub.docker.com/_/cassandra?tab=description&page=1&ordering=last_updated)