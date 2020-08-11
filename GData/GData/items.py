# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class serverItem(scrapy.Item):
    title = scrapy.Field()
    cpu = scrapy.Field()
    ram = scrapy.Field()
    ssd = scrapy.Field()
    thue = scrapy.Field()
    price = scrapy.Field()