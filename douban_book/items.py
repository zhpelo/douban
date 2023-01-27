# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    table   = 'book'
    isbn      = scrapy.Field()
    title       = scrapy.Field()
    origin_title = scrapy.Field()
    subtitle    = scrapy.Field()
    image       = scrapy.Field()
    author      = scrapy.Field()
    translator  = scrapy.Field()
    publisher   = scrapy.Field()
    pubdate     = scrapy.Field()
    binding     = scrapy.Field()
    price       = scrapy.Field()
    series      = scrapy.Field()
    pages       = scrapy.Field()
    author_intro = scrapy.Field()
    catalog     = scrapy.Field()
    summary     = scrapy.Field()
    tags        = scrapy.Field()
    rating      = scrapy.Field()
    grab_time   = scrapy.Field()
    grab_url    = scrapy.Field()
    status      = scrapy.Field()

