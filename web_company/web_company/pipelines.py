# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class WebCompanyPipeline:
    def process_item(self, item, spider):
        return item


class MongoPipeline:
    def open_spider(self, spider):
        #self.mymongo = pymongo.MongoClient("mongodb://root:123@localhost:27017/")
        self.mymongo = pymongo.MongoClient("mongodb://root:123@mongodb:27017/")
   
        self.mydb = self.mymongo["bar"]
        # self.mydb.command('ping')
        self.mycol = self.mydb["book1"]

    def process_item(self, item, spider):
        mydict = {"name": item['name'][0],
                    "url": None if item.get('url')==None else item.get('url')[0]}
        self.mycol.insert_one(mydict)

    def close_spider(self, spider):
        self.mymongo.close()
