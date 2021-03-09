# test-django

## Environment Setup

**Important:** Update the following line(s) on `.env` file:

```
USAGE_LOGGERS_URL = https://<resurface-host>:<port>/message
```

- Don't set USAGE*LOGGERS_URL to `localhost` (your Resurface database isn't running inside \_this* container)
- For maximum performance, leave out USAGE_LOGGERS_URL to disable loggers completely

## Docker Deployment

Run the following command in bash to get started:

```
make
```

Cleanup commands

```
make stop
make down

docker rm hackernews_django
```

View Logs

```
docker logs -f hackernews_django
```

## Heroku Deployment

```
heroku create XXX-resurface
heroku container:login
heroku container:push web
heroku container:release web
heroku config:set WORKERS=2
heroku config:set USAGE_LOGGERS_URL="http://marina:4001/message"
curl "http://XXX-resurface.herokuapp.com/ping"
heroku apps:destroy XXX-resurface
```
