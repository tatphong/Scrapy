# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import glob
import csv
import MySQLdb


class QuotesSpiderPipeline:
    def process_item(self, item, spider):
        return item

class DB_Save:
    mydb = MySQLdb.connect(
        host = 'localhost',
        user = 'admin_scrapy',
        password = '1q2w3e4R',
        db = 'scrapy_db',
    )
    cursor = mydb.cursor()

    def process_item(self, item, spider):
        self.cursor.execute('Insert into books (name, price, tax) values (%s, %s, %s)',
                                (item['name'], item['price'], item['tax'])
                            )
        self.mydb.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.mydb.close()

class DB_Save_comment:
    mydb = MySQLdb.connect(
        host = 'localhost',
        user = 'admin_scrapy',
        password = '1q2w3e4R',
        db = 'scrapy_db',
        charset = 'utf8',
    )
    cursor = mydb.cursor()

    def process_item(self, item, spider):
        for i in item['cmt']:
            i=i.strip()
            if i == "":
                continue
            query = 'Insert into comment_db (comment) values ("'+i+'")'
            print (query)
            self.cursor.execute(query)
        self.mydb.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.mydb.close()