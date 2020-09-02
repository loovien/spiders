#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @title: 
# @author: luowen<loovien@163.com>
# @website: https://loovien.github.com
# @time: 9/2/2020 10:19 PM

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from videos.spiders import weibo

if __name__ == '__main__':
    configure_logging()
    runner = CrawlerRunner()
    runner.crawl(weibo.WeiBoSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
