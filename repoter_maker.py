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
    <link href="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/3.4.1/css/bootstrap-theme.min.css" rel="stylesheet">
    <style>
        table{
            margin: 0 auto;
        }
        .danger {
            color: #d9534f;
        }
    </style>
</head>

<body>
    <table class="table table-bordered table-hover">
        <tr>
            <th>信息</th>
            <th>数量</th>
        </tr>
        {% for info in info_list %}
        <tr>
            <td>{{info.name}}</td>
            <td  class="{{ info.class }}">{{info.count}}</td>
        </tr>
        {% endfor %}
    </table>
    <details>
        <table class="table table-bordered table-hover">
            <tr>
                <th>url</th>
                <th>响应结果</th>
                <th>响应体大小kb</th>
                <th>响应时间MS</th>
            </tr>

            {% for data in data_list %}
            <tr >
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
template = '''
<!DOCTYPE html>
<html lang="zh">

<head>
    <meta charset="UTF-8">
    <title>Http Check Report</title>
    <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" crossorigin="anonymous">
    
    <style>
        table {
            margin: 0 auto;
        }

        .danger {
            color: #d9534f;
        }
        /* body {
            width: 80%;
            margin: 0 auto;
        } */
    </style>
</head>

<body >
    <table class="table table-striped table-hover">
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
    <!-- <details> -->
        <table class="table table-bordered table-hover">
            <tr>
                <th>url</th>
                <th>响应结果</th>
                <th>响应体大小kb</th>
                <th>响应时间MS</th>
            </tr>

            {% for data in data_list %}
            <tr>
                <td>
                    <a href={{data.url}}>{{data.url}}</a>
                </td>
                <td>{{data.status}}</td>
                <td>{{data.size}}</td>
                <td>{{data.time}}</td>
            </tr>
            {% endfor %}
        </table>
    <!-- </details> -->
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
            row["time"] = int(row["time"])
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
        if k in fail_status_code:
            is_danger = "danger"
        else:
            is_danger = ""
        info_list.append({"name": "请求状态码为" + k + "的数量", "count": v, "class": is_danger})
    report = Template(template)
    data_result = list(sorted(data_result, key=lambda e: e.__getitem__('time'), reverse=True))
    result = report.render(data_list=data_result, info_list=info_list)
    with open("report.html", "w") as f:
        f.write(result)
    assert the_result, "出现错误状态码！！！！"


if __name__ == "__main__":
    make_report()
