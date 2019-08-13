# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import logging
from .items import DockerpyspiderItem

class DockerpyspiderPipeline(object):

    def open_spider(self, spider):
        if (spider.name == "SampleSpider"):
            logging.error("----open spider")
            self.client = pymongo.MongoClient(host="mongodb", port=27017)
            self.db = self.client["DailyProject"]
            self.collection = self.db["3dmcollection"]

    def process_item(self, item, spider):
        if isinstance(item, DockerpyspiderItem):
            try:
                self.collection.insert(dict(item))
                logging.info("items: " + item['title'] + " has INSERTED in ACTRESS db.")
            except Exception as e:
                logging.error("PIPLINE EXCEPTION: JavpopActressItem: " + str(e))
        return item


    def close_spider(self, spider):
        if self.client is not None:
            self.client.close()
