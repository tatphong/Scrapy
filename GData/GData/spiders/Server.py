import scrapy
from GData.items import serverItem
from scrapy.loader import ItemLoader



class ServerSpider(scrapy.Spider):
    name = 'Server'
    allowed_domains = ['www.gdata.com.vn']
    start_urls = ['https://www.gdata.com.vn/cloud-server/']

    def parse(self, response):
        tiso = [1, 0.975, 0.95, 0.9]

        titles =  response.xpath('//*[@id="section-cloudserver"]/.//*[@class="item-title"]/text()').extract()
        cate_cpu = response.xpath('//*[contains(@class,"cpu")]/@name').extract()
        cate_ram = response.xpath('//*[contains(@class,"ram")]/@name').extract()
        cate_ssd = response.xpath('//*[contains(@class,"ssd")]/@name').extract()

        for index, title in range(titles):
            months = response.xpath('//*[@class="item-price-promotion"]/.//li/text()').extract()
            prices = response.xpath('//*[@name="'+ cate_cpu[index] +'"]/../../../following-sibling::div[@class="item-price-promotion"]/.//span[1]/text()').extract()
            cpus = response.xpath('//*[@name="'+ cate_cpu[index] +'"]/option/text()').extract()
            cpu_prices = response.xpath('//*[@name="'+ cate_cpu[index] +'"]/option/@data-price').extract()
            rams = response.xpath('//*[@name="'+ cate_ram[index] +'"]/option/text()').extract()
            ram_prices = response.xpath('//*[@name="'+ cate_ram[index] +'"]/option/@data-price').extract()
            ssds = response.xpath('//*[@name="'+ cate_ssd[index] +'"]/option/text()').extract()
            ssd_prices = response.xpath('//*[@name="'+ cate_ssd[index] +'"]/option/@data-price').extract()
            for i, cpu in enumerate(cpus):
                for j, ram in enumerate(rams):
                    for k, ssd in enumerate(ssds):
                        for l, price in enumerate(prices):
                            # print("**********************",index,i,j,k,l)
                            # print(tiso[l], cpu_prices[i])
                            update_price = round(int(price.replace(".","")) + float(int(cpu_prices[i]) 
                                                + int(ram_prices[j]) + int(ssd_prices[k])) * tiso[l])

                            data = ItemLoader(item = serverItem(), response=response)
                            data.add_value('title', title)
                            data.add_value('cpu', cpu)
                            data.add_value('ram', ram)
                            data.add_value('ssd', ssd)
                            data.add_value('thue', months[l])
                            data.add_value('price', update_price)
                            yield data.load_item()
