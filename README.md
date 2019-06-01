# test-django-heroku

This was cloned from Heroku's [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python) app at commit `2fde3b4`. We prefer to keep our own copy to keep our tests from breaking without warning.

To run locally:

```
brew services start postgresql
createdb python_getting_started

python3 -m venv getting-started
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic

heroku local
```
