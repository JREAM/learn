from django.db import models


class Authors(models.model):
    name = models.CharField(max_length=30)


class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Authors)
