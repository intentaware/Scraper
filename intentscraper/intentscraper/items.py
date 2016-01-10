# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from apps.metas.models import ScrapedData, DomainData


class IntentscraperItem(DjangoItem):
    django_model = ScrapedData

class DomainItem(DjangoItem):
    django_model = DomainData

