SHELL := /bin/bash # Use bash syntax

install:
	pip install poetry && \
	poetry install


test:
	pytest --cov=git_repo_sync tests/

build:
	docker-compose -f docker-compose.yml build

serve:
	docker-compose -f docker-compose.yml up --build -d

serve-aws:
	docker-compose -f docker-compose.aws.yml up --build -d

migrate:
	docker-compose run git_repo_sync-api alembic upgrade head

bash:
	docker-compose run git_repo_sync-api bash

logs:
	docker-compose logs -f git_repo_sync-api