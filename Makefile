# Makefile for Dockerized FastAPI project

# Variables
DOCKER_COMPOSE = docker-compose
SERVICE_NAME = fastapi_app

# Targets
.PHONY: build start stop test clean

# Build Docker containers
build:
    $(DOCKER_COMPOSE) build

# Start Docker containers in detached mode
start:
    $(DOCKER_COMPOSE) up -d

# Stop and remove Docker containers
stop:
    $(DOCKER_COMPOSE) down

# Run tests using pytest inside the Docker container
test:
    $(DOCKER_COMPOSE) exec $(SERVICE_NAME) pytest

# Clean up Docker volumes and networks
clean:
    $(DOCKER_COMPOSE) down -v --remove-orphans

# Additional commands as needed
