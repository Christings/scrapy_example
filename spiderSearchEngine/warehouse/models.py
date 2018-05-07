from __future__ import unicode_literals
from django.db import models


# Create your models here.
class TestScrapy(models.Model):
    url = models.TextField(max_length=255)
    title = models.CharField(max_length=255)
    abstract = models.TextField()

    class Meta:
        app_label = 'warehouse'
        db_table = 'test_scrapy'


