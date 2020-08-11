# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class GdataPipeline:
    def process_item(self, item, spider):
        return item

class cleanData:
    def cleanItem(self, a):
        a = a.replace("\n", "")
        a = a.strip()
        a = re.sub(r'[  ]',' ',a)
        return a

    def process_item(self, item, spider):
        # for each_item in item:
        #     each_item = each_item.replace("\n", "")
        #     each_item = each_item.strip()
        #     each_item = re.sub(r'[  ]',' ',each_item)
        #     print(each_item)
        # print ("00000000000000000", item['title'])
        item['title'][0] = self.cleanItem(item['title'][0])
        item['cpu'][0] = self.cleanItem(item['cpu'][0])
        item['ram'][0] = self.cleanItem(item['ram'][0])
        item['ssd'][0] = self.cleanItem(item['ssd'][0])
        item['thue'][0] = self.cleanItem(item['thue'][0])
        return item
