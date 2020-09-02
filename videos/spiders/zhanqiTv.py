import scrapy


class ZhanqitvSpider(scrapy.Spider):
    name = 'zhanqiTv'
    allowed_domains = ['www.zhanqi.tv']
    start_urls = ['http://www.zhanqi.tv/lives']

    def parse(self, response):
        pass
