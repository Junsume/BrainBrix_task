# Makefile for Celery Docker project

# Variables
PROJECT_NAME = celery_app
DOCKER_COMPOSE = docker-compose

# Build Docker images
build:
	$(DOCKER_COMPOSE) build

# Start the services (web, celery, redis)
up:
	$(DOCKER_COMPOSE) up -d

# Stop the services
down:
	$(DOCKER_COMPOSE) down

# Rebuild and restart everything
restart: down build up

# Show logs
logs:
	$(DOCKER_COMPOSE) logs -f

# Run celery worker (used inside container or override)
worker:
	$(DOCKER_COMPOSE) run --rm web celery -A app.celery_app worker --loglevel=info

# Open a bash shell in the web container
bash:
	$(DOCKER_COMPOSE) exec web bash

# Remove all containers, networks, volumes, images
prune:
	docker system prune -af --volumes

# Run a task manually using Python
task:
	$(DOCKER_COMPOSE) run --rm web python -c "from app.tasks import add; print(add.delay(2, 3))"
