# test-django-heroku

## Docker Build

```
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate --run-syncdb
docker build -t test-django-heroku .
deactivate
```

## Docker Deployment

```
docker run --env-file .env test-django-heroku sh -c "python manage.py makemigrations && python manage.py migrate --run-syncdb"
docker run --env-file .env -p 80:8000 test-django-heroku
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
