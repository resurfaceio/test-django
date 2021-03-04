FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind :$PORT --workers $WORKERS django_integration_test.wsgi:application