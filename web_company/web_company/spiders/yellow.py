import scrapy
from web_company.items import CompanyInfoItem
from scrapy.loader import ItemLoader


class YellowSpider(scrapy.Spider):
    name = 'yellow'
    allowed_domains = ['yellowpages.vnn.vn']
    start_urls = [
        'https://www.yellowpages.vnn.vn/tgcls/40132120/danh-sach-cong-ty-thiet-ke-website.html?page=1&i=3']
    custom_settings = {
        # 'DOWNLOAD_DELAY': 2,
        'ITEM_PIPELINES': {
            'web_company.pipelines.MongoPipeline': 300
        }
    }

    def parse(self, response):
        names = response.xpath('//h2/a/text()').extract()
        # urls =  response.xpath('//*[@class="listing_website"]/a[@rel="nofollow"]/@href').extract()
        for name in names:
            loader = ItemLoader(item=CompanyInfoItem(), response=response)
            url = response.xpath(
                '//h2/a[text()="'+name+'"]/../../../.././/*[@class="listing_website"]/a[@rel="nofollow"]/@href').extract()
            loader.add_value('name', name)
            loader.add_value('url', url)
            yield loader.load_item()

        next_page_url = response.xpath(
            '//a[text()="Tiếp"]/@href').extract_first()
        # print(next_page_url)
        if next_page_url == "?page=151&i=3":
            return True
        absolute_next = self.start_urls[0].replace(
            self.start_urls[0].split("html")[1], next_page_url)
        yield scrapy.Request(absolute_next)
        # absolute_next = response.replace(self.start_urls[0].split('?')[0] + next_page_url)
        # yield scrapy.Request.replace(self.start_urls[0].split('?')[0] + next_page_url)
