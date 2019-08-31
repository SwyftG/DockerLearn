# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import DockerpyspiderItem
from scrapy.selector import Selector


class SamplespiderSpider(scrapy.Spider):
    name = 'SampleSpider'
    allowed_domains = ['example.com']
    start_urls = ['https://cc.wpio.xyz/']

    def start_requests(self):
        # block_url = "https://cc.wpio.xyz/thread0806.php?fid=7"
        block_url = "https://www.3dmgame.com/"
        yield Request(url=block_url, callback=self.parse_block_page, dont_filter=True)

    def parse_block_page(self, response):
        news_list = response.xpath("//div[@class='Listwrap']//a").extract()
        for content_item in news_list:
            selector = Selector(text=content_item)
            spider_item = DockerpyspiderItem()
            spider_item['title'] = selector.xpath("//text()").extract_first()
            spider_item['url'] = selector.xpath("//@href").extract_first()
            # print(spider_item)
            yield spider_item