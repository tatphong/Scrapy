import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['sso.garena.com']
    start_urls = ['https://sso.garena.com/ui/login?app_id=10100&redirect_uri=https%3A%2F%2Faccount.garena.com%2F%3Flocale_name%3DVN&locale=vi-VN']

    def parse(self, response):
        # csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        yield FormRequest('https://sso.garena.com/ui/login?app_id=10100&redirect_uri=https%3A%2F%2Faccount.garena.com%2F%3Flocale_name%3DVN&locale=vi-VN',
                            formdata = {
                                # 'csrf_token': csrf_token,
                                'username': "tattranphong",
                                'password': ""
                            },
                            callback=self.parse_after_login)

    def parse_after_login(self, response):
        self.log(response.xpath('//a/text()')[1].extract())
        if response.xpath('//a/text()')[1].extract() == "Logout":
            self.log("okeeeeeeeeeeeeeeeeeeee")
        else:
            self.log("wronggggggggggggg")
        open_in_browser(response)

