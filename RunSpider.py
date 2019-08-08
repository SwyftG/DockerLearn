# encoding: utf-8
__author__ = 'lianggao'
__date__ = '2018/5/11 上午11:27'

from scrapy import cmdline


def run_spider():
    cmdline.execute("scrapy crawl SampleSpider".split())

if __name__ == '__main__':
    run_spider()
