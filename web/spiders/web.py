#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import scrapy
from scrapy_splash import SplashRequest


# docker run -p 8050:8050 -e HTTP_PROXY=http://192.168.84.168:8899  -e HTTPS_PROXY=http://192.168.84.168:8899 -e http_proxy=http://192.168.84.168:8899 -e https_proxy=http://192.168.84.168:8899 scrapinghub/splash

class WebSpider(scrapy.Spider):
    name = 'web'
    custom_settings = {
        # 'DOWNLOAD_DELAY': 10,
        # 非机器人设置
        "ROBOTSTXT_OBEY": False
    }

    def start_requests(self):
        urls = [
            'https://www.baidu.com',
            'https://test121.meishubao.com/admin/login.html?app=admin&ret=%2Fadmin%2Fmybook.html'
        ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.net_page())

    def net_page(self):
        pass
