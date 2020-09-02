#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @title:  web spider
# @author: luowen<loovien@163.com>
# @website: https://loovien.github.com
# @time: 9/2/2020 10:17 PM

from scrapy.responsetypes import Response
from scrapy.spiders import Spider
from videos.items import ImageItem
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy_selenium import SeleniumRequest
from shutil import which


class WeiBoSpider(Spider):
    name = "weibo"

    custom_settings = {
        "IMAGES_STORE": "E:/codelab/python/spiders/output/images",
        "IMAGES_MIN_HEIGHT": 100,
        "IMAGES_MIN_WIDTH": 100,
        "SELENIUM_DRIVER_NAME": "chrome",
        "SELENIUM_DRIVER_EXECUTABLE_PATH": which("chromedriver"),
        "SELENIUM_DRIVER_ARGUMENTS": ["--headless"]
    }

    def start_requests(self):
        return [SeleniumRequest(
            url="https://weibo.com/?category=10011",
            wait_time=10,
            wait_until=EC.presence_of_element_located((By.CSS_SELECTOR, ".UG_list_b")))
        ]

    def parse(self, response: Response, **kwargs):
        for box in response.xpath("//div[@class='imgBox']/img"):
            yield ImageItem(image_urls=[box.xpath("./@src").extract()])
