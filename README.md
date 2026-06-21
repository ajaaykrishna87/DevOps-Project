# Flask DevOps Project

A simple Flask application containerized using Docker.

## Features

- Flask REST API
- Dockerized Application
- Health Check Endpoint
- Version Endpoint

## Endpoints

### Home

GET /

Returns application status.

### Health

GET /health

Returns application health.

### Version

GET /version

Returns application version.

## Build Docker Image

docker build -t flask-devops-app:v1 .

## Run Docker Container

docker run -d --name flask-app -p 5000:5000 flask-devops-app:v1
