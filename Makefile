dc = docker-compose

run:
	$(dc) up -d

build:
	docker build ./mailing -t mailing_app

local:
	python mailing/manage.py runserver

test:
	$(dc) run --rm app python -m pytest

migrate:
	$(dc) run --rm app python manage.py makemigrations && python manage.py migrate