import scrapy
from quotes_spider.items import Comment
from scrapy.loader import ItemLoader

class Books2Spider(scrapy.Spider):
    name = 'books2'
    allowed_domains = ['diendantoanhoc.net']
    start_urls = ['https://diendantoanhoc.net/topic/189478-t%C3%ACm-c%C3%A1-voi-b%E1%BA%B1ng-%C4%91%E1%BB%8Bnh-l%C3%BD-pythagoras/']

    def parse(self, response):
        cmt = response.xpath('//*[@itemprop="commentText"]/p/text()').extract()
        data = ItemLoader(item = Comment(), response = response)
        data.add_value('cmt',cmt)
        return data.load_item()

    def parsedata(self, response):
        pass