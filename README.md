# test-django
Test GraphQL API built with Django 

## Configure Environment

Install your Resurface database: https://resurface.io/pilot-edition

```
# configure to point to your Resurface database host
export USAGE_LOGGERS_URL=http://<resurface-host>:4001/message
```

## Deploy Locally

```
make start     # rebuild and start containers
make ping      # make simple ping request
make bash      # open shell session
make logs      # follow container logs
make stop      # halt and remove containers
```

## Deploy to Heroku

1. Create Heroku app
```
heroku create django-resurface
```

2. Push to Heroku
```
heroku container:login
heroku container:push web
heroku container:release web
heroku config:set WORKERS=2
heroku config:set USAGE_LOGGERS_URL=$USAGE_LOGGERS_URL
```

3. Make ping request
```
curl "http://django-resurface.herokuapp.com/ping"
```

4. Delete Heroku app
```
heroku apps:destroy django-resurface
```
