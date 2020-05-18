
build:
	docker-compose up --build -d

up:
	docker-compose up

db-make-migrations:
	docker-compose exec django-app python manage.py makemigrations

db-migrate:
	docker-compose exec django-app python manage.py migrate

create-superuser:
	docker-compose exec django-app python manage.py createsuperuser

stop-all:
	docker-compose down

# app-start:
# 	docker-compose exec web python manage.py runserver 0.0.0.0:8080

