import scrapy
import re


class HireSpider(scrapy.Spider):
    name = 'Hire'
    allowed_domains = ['vndata.vn/server/thue-may-chu']
    start_urls = ['http://vndata.vn/server/thue-may-chu/']

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

            ans['Name'] = self.cleanString(item)
            ans['Price'] = self.cleanString(prices[i])

            bot = response.xpath('//*[@class="it-bot"]')[i]
            lis = bot.xpath('.//li')
            # li 0
            ans['Server'] = self.cleanString(
                lis[0].xpath('.//text()')[1].extract())
            # li  1:4
            for i in range(1, 5):
                value = lis[i].xpath('.//text()').extract()
                ans[value[1][:-1]] = self.cleanString(value[2])
            # li 5,6
            for i in range(5, 7):
                value = lis[i].xpath('.//text()').extract_first()
                value = self.cleanString(value)
                divide = value.split(': ')
                ans[divide[0]] = divide[1]
            yield ans
