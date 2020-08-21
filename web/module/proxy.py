#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from mitmproxy import http
import os
import time

PATH = os.path.dirname(os.path.abspath(__file__))


class Web:
    def __init__(self):
        self.file_name = "data"
        self.file_path = PATH + "/../recording/" + self.file_name + ".csv"
        self.f = open(self.file_path, "w")
        self.recording = ["url,status,size,time\n"]

    def response(self, flow: http.HTTPFlow):
        url = flow.request.url
        status_code = flow.response.status_code
        spend_time = int((flow.response.timestamp_end - flow.request.timestamp_start) * 1000)
        response_size = len(flow.response.raw_content) if flow.response.raw_content else 0
        self.recording.append(
            url + "," + str(status_code) + "," + str(int(response_size/1024)) + "," + str(spend_time) + "\n")

    def done(self):
        self.f.writelines(self.recording)
        self.f.close()
