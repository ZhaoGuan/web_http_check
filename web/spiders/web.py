#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Gz'
import scrapy
from scrapy_splash import SplashRequest
import requests


# docker run -p 8050:8050 -e HTTP_PROXY=http://192.168.84.168:8899  -e HTTPS_PROXY=http://192.168.84.168:8899 -e http_proxy=http://192.168.84.168:8899 -e https_proxy=http://192.168.84.168:8899 scrapinghub/splash


def url_data(source="test"):
    login_url = {
        "boss": "/admin/login.php",
        "boss1": "/admin/login.php",
        "cms": "/ken/login.php",
    }
    user_data = {"test": {
        "boss": {
            "username": "392",
            "password": "123456"
        },
        "boss1": {
            "username": "392",
            "password": "123456"
        },
        "cms": {
            "username": "392",
            "password": "123456"
        },
    }}
    host_data = {
        "test": {
            "boss": "https://test121.meishubao.com",
            "boss1": "https://test121new.meishubao.com",
            "cms": "https://jiaoyantest.meishubao.com"
        },
    }
    url_data = {
        "boss": [
            "/admin/mybook.html",
            "/admin/u_userinfo_home.html?id=1798303",
            "/1v1boss#/ClassBill/index?userid=1798303",
            "/admin/deane_ducation.html#/DeanEducation",
            "/admin/u_userinfo.html",
            "/admin/u_student_list.html?tag_id=all&",
        ],
        "boss1": ["/r_reserve2?user=1791256&times="
                  "/s_user?user=1791256",
                  "/s_teacher?teacher=373"],
        "cms": ["/"
                "/teach_research/educational/series",
                "/teach_research/label/list"],
    }
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
