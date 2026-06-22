#!/bin/bash

apt-get update -y
apt-get install -y docker.io

systemctl enable docker
systemctl start docker

usermod -aG docker ubuntu

docker run -d \
--name nginx-demo \
-p 80:80 \
nginx
