# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidNepalItem(scrapy.Item):
    # define the fields for your item here like:
    country = scrapy.Field()
    confirmed = scrapy.Field()
    deaths = scrapy.Field()
    recovered = scrapy.Field()
    active = scrapy.Field()
