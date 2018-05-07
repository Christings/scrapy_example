import scrapy
from scrapy_djangoitem import DjangoItem
from warehouse.models import TestScrapy

# class KeywordspiderItem(scrapy.Item):
#     url = scrapy.Field()
#     title = scrapy.Field()
#     abstract = scrapy.Field()


class KeywordspiderItem(DjangoItem):
    django_model = TestScrapy