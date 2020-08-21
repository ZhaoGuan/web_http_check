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
</body>
</html>
'''
PATH = os.path.dirname(os.path.abspath(__file__))


def make_report():
    data_result = []
    with open(PATH + "/web/recording/data.csv")as f:
        data = csv.DictReader(f)
        for row in data:
            data_result.append(row)
    report = Template(template)
    result = report.render(data_list=data_result)
    with open("report.html", "w") as f:
        f.write(result)


if __name__ == "__main__":
    make_report()
