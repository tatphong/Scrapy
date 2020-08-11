import scrapy
import os
import glob
import csv
import MySQLdb
from quotes_spider.items import Data_item
from scrapy.loader import ItemLoader

class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books_url = response.xpath('//h3/a/@href').extract()
        for book in books_url:
            absolute_url = response.urljoin(book)
            yield scrapy.Request(absolute_url, callback = self.parsedata)

        # next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        # absolute_next_url = response.urljoin(next_page_url)
        # yield scrapy.Request(absolute_next_url)

    def parsedata(self, response):
        data = ItemLoader(item = Data_item(), response = response)
        name = response.xpath('//h1/text()').extract()
        price = response.xpath('//*[@class="price_color"]/text()').extract_first()
        tax = response.xpath('//*[@class="table table-striped"]/tr[5]/td/text()').extract()
        
        data.add_value('name', name)
        data.add_value('price', price)
        data.add_value('tax', tax)
        return data.load_item()

    # @staticmethod
    # def close(reason):
    #     csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        
    #     mydb = MySQLdb.connect(
    #         host = 'localhost',
    #         admin = 'admin_scrapy',
    #         password = '1q2w3e4R',
    #         db = 'scrapy_db',
    #         charset = 'utf-8'
    #     )
    #     cursor = mydb.cursor()

    #     row_count = 0
    #     csv_data = csv.reader(file(csv_file))
    #     for row in csv_data:
    #         if row_count != 0:
    #             cursor.execute('Insert into books (name, price, tax) values (%s, %s, %s)', row)
    #         row_count += 1
    #         yield row

    #     print ("**************************************",csv_data[0])

    #     mydb.commit()
    #     cursor.close()
    #     mydb.close()
