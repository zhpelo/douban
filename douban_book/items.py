# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    table   = 'book'
    douban_id   = scrapy.Field()
    isbn13      = scrapy.Field()
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

    # url = scrapy.Field()
    # title = scrapy.Field()
    # subtitle = scrapy.Field()
    # author = scrapy.Field()
    # publishing_year = scrapy.Field()
    # publishing_house = scrapy.Field()
    # page_number = scrapy.Field()
    # price = scrapy.Field()
    # isbn = scrapy.Field()
    # rating = scrapy.Field()
    # vote_number = scrapy.Field()
    # image = scrapy.Field()
    # content_intro = scrapy.Field(comment='内容简介')
    # author_intro = scrapy.Field()
    # directory = scrapy.Field()
    # tags = scrapy.Field()

