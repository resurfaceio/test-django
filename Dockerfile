FROM python:3.7

WORKDIR /app

ADD . /app
RUN pip install -r requirements.txt && pip install git+https://github.com/resurfaceio/logger-python
RUN python manage.py makemigrations && python manage.py migrate --run-syncdb

EXPOSE 8000