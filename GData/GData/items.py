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


class ColocationItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    spacerack = scrapy.Field()
    electric = scrapy.Field()
    ip = scrapy.Field()
    datatransfer = scrapy.Field()
    bandwidthnix = scrapy.Field()
    bandwidthnation = scrapy.Field()
    port = scrapy.Field()
    online = scrapy.Field()
    security = scrapy.Field()
    technique = scrapy.Field()
    initprice = scrapy.Field()
    server = scrapy.Field()
