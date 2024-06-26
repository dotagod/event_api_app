# Event API Project

This project provides an API endpoint that fetches event data from an external XML API, filters events by date range, and caches the results using Redis. The API is built using FastAPI and utilizes Redis for caching and Docker for containerization.

## Project Overview

- **API Endpoint**: The project fetches events from an external API endpoint (`https://provider.code-challenge.feverup.com/api/events`) and provides a new endpoint to filter events based on a date range.
- **Caching**: The fetched events are stored in Redis for quick access in future queries.
- **Filtering**: Only events with `sell_mode` set to `online` are returned.
- **Technology Stack**: FastAPI, Redis, Docker, asyncio.

## Directory Structure

├── app  
│ ├── api  
│ │ ├── events.py  
│ │ ├── init.py  
│ ├── models  
│ │ ├── event.py  
│ │ ├── init.py  
│ ├── services  
│ │ ├── event_service.py  
│ │ ├── redis_service.py  
│ │ ├── init.py  
│ ├── main.py  
├── tests  
│ ├── test_main.py  
├── Dockerfile  
├── docker-compose.yml  
├── Makefile  
└── README.md  

## Makefile Commands

The Makefile provides several commands to manage the project:

- **build**: Builds the Docker images using `docker-compose`.
  ```sh
  make build

  make start

  make stop

  make clean

  make test


If you prefer to use Docker commands directly, you can perform the same actions as the Makefile commands:

```sh
  docker-compose build
  docker-compose up -d
  docker-compose down
  docker-compose down --rmi all --volumes --remove-orphans
```

## Swagger API Documentation

The project includes automatically generated API documentation using Swagger UI. This documentation provides an interactive interface to explore and test the API endpoints.

### Accessing Swagger Documentation

Once the application is running, you can access the Swagger UI at the following URL:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)

The Swagger UI provides a user-friendly interface where you can see all the available API endpoints, their expected parameters, and response formats. You can also test the endpoints directly from the browser.

### Example of an Endpoint with Default Parameters

For example, the `/events` endpoint allows you to filter events by date range with default values for `starts_at` and `ends_at` parameters:


# Scaling the Event API Application

## Introduction

This section provides an overview of strategies to scale the Event API application to handle high traffic and large datasets. While the current implementation is suitable for small-scale testing, scaling it for production environments with thousands of events and peak traffic of 5k to 10k requests per second requires additional considerations and optimizations.

## Performance Optimization Strategies

### 1. Load Balancing

Distribute incoming traffic across multiple instances of the application using a load balancer. Common solutions include:

- **NGINX**: Acts as a reverse proxy and load balancer.
- **HAProxy**: High-performance load balancer.
- **Cloud Load Balancers**: AWS ELB, Google Cloud Load Balancer, etc.

### 2. Horizontal Scaling

Deployment on multiple instances of the application to handle increased traffic. Using container orchestration tools like Kubernetes to manage and scale the deployment. This ensures that the application can handle more requests by running multiple copies of it.

### 3. Database Optimization

Integration with a database for persistent storage, optimized read and write performance:

- **Indexing**: Create indexes on frequently queried fields to speed up read operations.
- **Sharding**: Distribute data across multiple database instances to balance the load.
- **Replication**: Use read replicas to distribute read traffic, ensuring the master database handles only write operations.

### 4. Rate Limiting

Implement rate limiting to protect the application from being overwhelmed by excessive requests:

- **FastAPI Rate Limiter**: Use middleware to limit the number of requests per client.
- **API Gateway**: Use an API gateway (e.g., AWS API Gateway) to enforce rate limits at the edge, reducing the load on your application.

### 5. Monitoring and Logging

Set up monitoring and logging to track the performance and health of the application:

- **Monitoring Tools**: Tools like Prometheus and Grafana can be used to monitor the application's metrics and visualize its performance in real time.
- **Logging**: Use structured logging and log aggregation tools (e.g., ELK stack) to collect and analyze logs, helping you troubleshoot and understand the application's behavior under load.

### 6. Content Delivery Network (CDN)

Use a CDN to cache and serve static content closer to users, reducing latency and load on the origin server. This is especially useful for serving static assets such as images, scripts, and stylesheets.

