# test-django-heroku

## Run project locally

```
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install git+https://github.com/resurfaceio/logger-python
python manage.py makemigrations
python manage.py migrate --run-syncdb
deactivate
```

## Run project on Docker

```
docker build -t test-django-heroku . --no-cache
docker run --env-file .env -d -p 80:8000 --name test-django-heroku -t test-django-heroku
docker container exec -it  test-django-heroku bash
```
Run the following migrations inside docker bash

```
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
```

Now you can access the app from: `http://localhost/`

## Heroku Deployment

```
heroku container:login
heroku container:push web --app $HEROKU_APP_NAME
heroku container:release web --app $HEROKU_APP_NAME
heroku config:set WORKERS=2 --app $HEROKU_APP_NAME
```

# HTTP Health Check

Request:

```
curl http://localhost:8000/ping
```

Response:

```
{"msg": "pong"}
```
