CONTAINER_PREFIX=docker exec -it todo-api-web

run:
	${CONTAINER_PREFIX} python manage.py runserver

create-su:
	${CONTAINER_PREFIX} python manage.py createsuperuser

makemigrations:
	${CONTAINER_PREFIX} python manage.py makemigrations

migrate:
	${CONTAINER_PREFIX} python manage.py migrate

run:
	docker-compose up

build:
	docker-compose build

force-build:
	docker-compose build --no-cache

build-and-run: build run

force-build-and-run: force-build run
