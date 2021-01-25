# test-django-heroku

This was cloned from Heroku's [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python) app at commit `2fde3b4`. We prefer to keep our own copy to keep our tests from breaking without warning.

## Running at Heroku

```
heroku create {appname}
git push heroku master
browse to http://{appname}.herokuapp.com
```

## Running locally

```
pip install git+https://github.com/resurfaceio/logger-python (or from local directory)
brew services start postgresql
createdb python_getting_started
python3 -m venv getting-started
env LDFLAGS='-L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/readline/lib' pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic
USAGE_LOGGERS_URL="http://localhost:4001/message" heroku local
pip uninstall usagelogger
```
