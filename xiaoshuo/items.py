# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CatalogItem(scrapy.Item):
    book_id = scrapy.Field() #id
    book_name = scrapy.Field() #名称

class XiaoshuoItem(scrapy.Item):
    book_id = scrapy.Field() #id
    chapte_id = scrapy.Field() #章节id
    chapte_name = scrapy.Field() #章节名称
    content = scrapy.Field() #章节内容
