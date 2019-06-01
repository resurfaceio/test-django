# test-django-heroku

This was cloned from Heroku's [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python) app at commit `2fde3b4`. We prefer to keep our own copy to keep our tests from breaking without warning.

To run locally:

```
brew services start postgresql
createdb python_getting_started

python -m venv getting-started
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic

heroku local
```
