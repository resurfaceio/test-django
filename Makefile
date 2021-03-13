PROJECT_NAME=hackernews

start:
	@docker-compose up --force-recreate --build --detach
	@docker exec -it hackernews python manage.py makemigrations
	@docker exec -it hackernews python manage.py migrate --run-syncdb

stop:
	@docker-compose stop
	@docker-compose down

bash:
	@docker exec -it hackernews bash

logs:
	@docker logs -f hackernews

ping:
	@echo curl "http://localhost/ping"
	@curl "http://localhost/ping"

restart:
	@docker-compose stop
	@docker-compose up
