dc = docker-compose

# build:
# 	$(dc) up --build

build:
	docker build ./mailing -t mailing_app

run:
	$(dc) up -d app

local:
	python mailing/manage.py runserver

test:
	$(dc) run --rm app python -m pytest