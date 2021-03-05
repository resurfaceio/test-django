# Integration testing app for python usagelogger

## Run the project (Development)

Note: You should be on the project root directory

### Create virtual env

```
python -m venv .venv
source .venv/bin/activate
```

### Install requirements

```
pip install -r requirements.txt
```

### Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

Important: If User table is not created then run the following command

```
python manage.py migrate --run-syncdb
```

## Docker Deployment

```
docker build -t django-integration-test:v0 .
docker run --env-file .env django-integration-test:v0 sh -c "python manage.py makemigrations && python manage.py migrate --run-syncdb"
docker run --env-file .env -p 80:8000 django-integration-test:v0
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

```bash
curl http://localhost:8000/ping
```

Response:

```
{"msg": "pong"}
```
