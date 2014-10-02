# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SavolItem(scrapy.Item):
    title = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()
    author = scrapy.Field()
    permalink = scrapy.Field()
    date = scrapy.Field()
