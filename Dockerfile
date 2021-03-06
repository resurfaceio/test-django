FROM python:3.7

COPY . .
RUN pip install -r requirements.txt && pip install git+https://github.com/resurfaceio/logger-python
RUN python manage.py makemigrations && python manage.py migrate --run-syncdb

CMD USAGE_LOGGERS_URL="$USAGE_LOGGERS_URL" gunicorn --bind :$PORT --workers $WORKERS django_integration_test.wsgi:application