#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Gz'
from jinja2 import Template
import os
import csv

template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Http Check Report</title>
</head>
<body>
<table border="1">
    <tr>
        <th>信息</th>
        <th>数量</th>
    </tr>
    {% for info in info_list %}
    <tr>
        <td>{{info.name}}</td>
        <td>{{info.count}}</td>
    </tr>
    {% endfor %}
</table>
<details>
    <table border="1">
        <tr>
            <th>url</th>
            <th>响应结果</th>
            <th>响应体大小kb</th>
            <th>响应时间MS</th>
        </tr>

        {% for data in data_list %}
        <tr>
            <td>
                {{data.url}}
            </td>
            <td>{{data.status}}</td>
            <td>{{data.size}}</td>
            <td>{{data.time}}</td>
        </tr>
        {% endfor %}
    </table>
</details>
</body>
</html>
'''
PATH = os.path.dirname(os.path.abspath(__file__))


def make_report():
    fail_status_code = ["404", "502"]
    the_result = True
    data_result = []
    with open(PATH + "/web/recording/data.csv")as f:
        data = csv.DictReader(f)
        url_count = 0
        status_count = {}
        time_out_count = 0
        for row in data:
            data_result.append(row)
            url_count += 1
            status = row["status"]
            spend_time = row["time"]
            if int(spend_time) > 1000:
                time_out_count += 1
            if status not in status_count.keys():
                status_count.update({status: 1})
            else:
                status_count[status] += 1
    info_list = [{"name": "共请求URL数量", "count": url_count},
                 {"name": "请求时间超过1S数量", "count": time_out_count}]
    for k, v in status_count.items():
        if k in fail_status_code:
            the_result = False
        info_list.append({"name": "请求状态码为" + k + "的数量", "count": v})
    report = Template(template)
    result = report.render(data_list=data_result, info_list=info_list)
    with open("report.html", "w") as f:
        f.write(result)
    assert the_result, "出现错误状态码！！！！"


if __name__ == "__main__":
    make_report()
