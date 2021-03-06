# test-django

## Docker Deployment

```
docker build -t test-django --no-cache .
docker run -d --name test-django -e USAGE_LOGGERS_URL="http://marina:4001/message" -e WORKERS=2 -e PORT=8000 -p 80:8000 test-django
curl "http://localhost/ping"
docker logs -f test-django
docker stop test-django
docker rm test-django
```
* Don't set USAGE_LOGGERS_URL to `localhost` (your Resurface database isn't running inside *this* container)
* For maximum performance, leave out USAGE_LOGGERS_URL to disable loggers completely

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
