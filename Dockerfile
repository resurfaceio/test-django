FROM python:3.7

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "django_integration_test.wsgi:application"]