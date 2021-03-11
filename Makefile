PROJECT_NAME=hackernews

start:
	@docker-compose up --force-recreate --build --detach
	@docker exec -it hackernews_django python manage.py makemigrations
	@docker exec -it hackernews_django python manage.py migrate --run-syncdb

stop:
	@docker-compose stop
	@docker-compose down
	@docker rmi hackernews_django

bash:
	@docker exec -it hackernews_django bash

logs:
	@docker logs -f hackernews_django

ping:
	@echo curl "http://localhost/ping"
	@curl "http://localhost/ping"

restart:
	@docker-compose stop
	@docker-compose up
