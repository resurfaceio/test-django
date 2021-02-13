# Integration testing app for python usagelogger

## Run the project (Development)

Note: You should be on the project root directory

### Create virtual env

```
$ python -m venv .venv
$ source activate ./.venv/bin/activate
```

### Install requirements

```
$ pip install requirements.txt
```

### Run migrations

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Important: If User table is not created then run the following command

```
$ python manage.py migrate --run-syncdb

```

## Docker Deployment

```
$ docker build -t django-integration-test:v0 .
$ docker run --env-file .env django-integration-test:v0 sh -c "python manage.py makemigrations && python manage.py migrate --run-syncdb"

$ docker run --env-file .env -p 80:8000 django-integration-test:v0


```
