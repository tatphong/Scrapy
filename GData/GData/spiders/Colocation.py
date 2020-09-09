import scrapy
from GData.items import ColocationItem
from scrapy.loader import ItemLoader


class ColocationSpider(scrapy.Spider):
    name = 'Colocation'
    allowed_domains = ['gdata.com.vn/cho-dat-server']
    start_urls = ['http://gdata.com.vn/cho-dat-server/']

    def parse(self, response):
        list = []
        for tableindex in range(1, 5):
            # catch table
            items = response.xpath(
                '//*[starts-with(@class,"section-server section-server-'+str(tableindex)+'")]/div/div/div/table')
            # catch thead
            names = items.xpath(
                './/thead/tr/th/text()')[1:].extract()
            # catch price
            prices = items.xpath(
                './/tbody/tr/td/span/text()').extract()
            # keys = items.xpath(
            #     './/tbody/tr/td[1]/text()')[:-1].extract()
            for index, name in enumerate(names):
                values = items.xpath(
                    './/tbody/tr/td['+str(index+2)+']/text()')[:-2].extract()

                # colocation = {}
                # colocation['name'] = name.replace('\t', '')
                # colocation['price'] = prices[index]
                # for index2, value in enumerate(values):
                #     value = value.strip()
                #     if value != '':
                #         colocation[keys[index2]] = value
                # yield colocation

                loader = ItemLoader(item=ColocationItem(), response=response)
                loader.add_value('name', name.replace('\t', ''))
                loader.add_value('price', prices[index])
                if len(values) < 6:
                    loader.add_value('spacerack', values[0])
                    loader.add_value('electric', values[1])
                    loader.add_value('server', values[2])
                    loader.add_value('technique', values[3])
                    loader.add_value('initprice', values[4])
                else:
                    loader.add_value('spacerack', values[0])
                    loader.add_value('electric', values[1])
                    loader.add_value('ip', values[2])
                    loader.add_value('datatransfer', values[3])
                    loader.add_value('bandwidthnix', values[4])
                    loader.add_value('bandwidthnation', values[5])
                    loader.add_value('port', values[6])
                    loader.add_value('online', values[7])
                    loader.add_value('security', values[8])
                    loader.add_value('technique', values[9])
                    loader.add_value('initprice', values[10])

                yield loader.load_item()
                # print(object)
