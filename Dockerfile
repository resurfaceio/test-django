FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt && pip install git+https://github.com/resurfaceio/logger-python

COPY . .

CMD gunicorn --bind :$PORT --workers $WORKERS django_integration_test.wsgi:application