# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeHomesweethomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


from scrapy_djangoitem import DjangoItem
from browse.models import Home, Screenshot, Distance



class HomeItem(DjangoItem):
    django_model = Home

class ScreenshotItem(DjangoItem):
    django_model = Screenshot
    
class DistanceItem(DjangoItem):
    django_model = Distance
    
