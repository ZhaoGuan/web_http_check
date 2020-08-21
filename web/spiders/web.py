#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import scrapy
from scrapy_splash import SplashRequest
import requests
import yaml
import os

PATH = os.path.dirname(os.path.abspath(__file__))


# docker run -p 8050:8050 -e HTTP_PROXY=http://192.168.84.168:8899  -e HTTPS_PROXY=http://192.168.84.168:8899 -e http_proxy=http://192.168.84.168:8899 -e https_proxy=http://192.168.84.168:8899 scrapinghub/splash


def url_data(source="test"):
    with open(PATH + "/../../url_data.yml") as f:
        data = yaml.safe_load(f)
    host_data = data["host_data"]
    url_data = data["url_data"]
    user_data = data["user_data"]
    login_url = data["login_url"]
    host = host_data[source]
    url_result = {}
    for key, value in url_data.items():
        for v_value in value:
            if key not in url_result:
                url_result[key] = [host[key] + v_value]
            else:
                url_result[key].append(host[key] + v_value)
    result = {}
    user_data = user_data[source]
    for key, value in login_url.items():
        url = host[key] + value
        data = user_data[key]
        response = requests.post(url, data=data)
        for url in url_result[key]:
            result[url] = response.headers
    return result


class WebSpider(scrapy.Spider):
    name = 'web'
    custom_settings = {
        # 'DOWNLOAD_DELAY': 10,
        # 非机器人设置
        "ROBOTSTXT_OBEY": False
    }

    def __init__(self, source=None, *args, **kwargs):
        super(WebSpider, self).__init__(*args, **kwargs)
        self.source = source

    def start_requests(self):
        data = url_data(self.source)
        for url, headers in data.items():
            yield SplashRequest(url=url, headers=headers, callback=self.net_page)

    def net_page(self, response):
        pass

