# Docker Swarm POC - Flask Application Deployment with GitLab CI/CD

This proof of concept demonstrates deploying a Flask application using Docker Swarm with CI/CD integration through GitLab.

## Overview

- A basic Flask application is containerized and deployed using Docker Swarm.
- The application runs as **three separate containers**, each exposed on **different ports**.
- Docker Swarm is used to manage the stack and services.

## Docker Swarm Commands Used

```bash
# Deploy the stack using the docker-compose file
docker stack deploy -c docker-compose.yml flask_stack

# List all deployed stacks
docker stack ls

# Display services within a specific stack
docker stack services <stack_name>

# List all running services
docker service ls

# Remove a specific service
docker service rm <service_name>

# Remove an entire stack
docker stack rm <stack_name>

```

## CI/CD Pipeline with GitLab

A `deployment.py` script is used to automate the Docker image build and deployment process.

### Pipeline Flow

- On every push to the `main` branch, the GitLab CI/CD pipeline is triggered.
- The pipeline performs the following steps:
  1. SSHs into the target VM using credentials (PEM file, user, and VM IP) stored as GitLab CI/CD variables.
  2. Executes the `deployment.py` script on the VM, which:
     - Pulls the latest code from the repository.
     - Builds a new Docker image with a dynamic tag based on the current timestamp (`%Y%m%d%H%M%S`).
     - Deploys the updated image to the Docker Swarm stack.