# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

class MovieItem(scrapy.Item):
    hoverlink_text = scrapy.Field()
    category_title = scrapy.Field()


class ScrapyBasicsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
