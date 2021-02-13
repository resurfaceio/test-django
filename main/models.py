from django.db import models

# Create your models here.


class Logs(models.Model):
    log = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
