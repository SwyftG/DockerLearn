# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import DockerpyspiderItem
import pymongo
import logging

class DockerpyspiderPipeline(object):
    def open_spider(self, spider):
        if (spider.name == "SampleSpider"):
            self.client = pymongo.MongoClient(host="mongodb", port=27017)
            self.db = self.client["TDMSpiderProject"]
            self.collection = self.db["3dmcollection"]

    def process_item(self, item, spider):
        if isinstance(item, DockerpyspiderItem):
            try:
                self.collection.insert(dict(item))
                logging.info("items: " + item['title'] + " has INSERTED in db.")
            except Exception as e:
                logging.error("PIPLINE EXCEPTION: DockerpyspiderItem: " + str(e))
        return item


    def close_spider(self, spider):
        if self.client is not None:
            self.client.close()