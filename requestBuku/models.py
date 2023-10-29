from django.db import models
from django.contrib.auth.models import User

class BukuReq(models.Model):
    title = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    language_code = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    publication_date = models.TextField(null=True, blank=True)
    publisher = models.TextField(null=True, blank=True)
