import scrapy
import re


class ColoSpider(scrapy.Spider):
    name = 'Colo'
    allowed_domains = ['vndata.vn/server/colo/']
    start_urls = ['http://vndata.vn/server/colo/']

    def cleanString(self, item):
        item = item.replace('\r', ' ')
        item = item.replace('\n', ' ')
        item = re.sub('\s+', ' ', item)
        item = item.strip()
        return item

    def parse(self, response):

        items = response.xpath(
            '//*[@class="it-top"]/p[@class="it-text"]/text()').extract()
        prices = response.xpath(
            '//*[@class="it-top"]/p[@class="it-title"]/text()').extract()
        response.xpath('//*[@class="it-bot"][1]/li/text()').extract()
        for i, item in enumerate(items):
            ans = {}
            isServer = True
            bot = response.xpath('//*[@class="it-bot"]')[i]
            values = bot.xpath('.//li/text()').extract()

            ans['Name'] = self.cleanString(item)
            ans['Price'] = self.cleanString(prices[i])

            for j, value in enumerate(values):
                if value.find(': ') >= 0:
                    value = self.cleanString(value)
                    divide = value.split(': ')
                    ans[divide[0]] = divide[1]
                else:
                    isServer = False
            if isServer:
                yield ans
            else:
                continue
