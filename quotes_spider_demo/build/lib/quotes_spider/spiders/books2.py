import scrapy


class Books2Spider(scrapy.Spider):
    name = 'books2'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield scrapy.Request(absolute_url, callback = self.parsebook)
        
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_url)

    def parsebook(self, response):
        pass