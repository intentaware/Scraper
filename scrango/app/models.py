from django.db import models
from model_utils.models import TimeStampedModel


class ScrapedData(TimeStampedModel):
    domain = models.CharField(max_length=255, null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    jsondata = models.TextField(null=True, blank=True)
