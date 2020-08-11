import scrapy
from Vndata.items import CloudItem
from scrapy.loader import ItemLoader



class CloudSpider(scrapy.Spider):
    name = 'Cloud'
    allowed_domains = ['clients.vndata.vn']
    start_urls = ['https://clients.vndata.vn/?/cart/cloud-server//']

    def parse(self, response):
        names = response.xpath('//h4[text()!="Đăng nhập"]/text()').extract()
        prices = response.xpath('//span[contains(@class,"h1")]/text()').extract()
        contents = response.xpath('//div[contains(@class,"p-1")]/text()').extract()

        step = 0
        index = 0
        while index < len(contents):
            cloud = ItemLoader(item = CloudItem(), response=response)
            cloud.add_value('name', names[step])
            cloud.add_value('price', prices[step])
            step += 1
            cloud.add_value('vcpu', contents[index+1])
            cloud.add_value('ram', contents[index+3])
            cloud.add_value('ssd', contents[index+5])
            index += 6
            yield cloud.load_item()
