# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import subprocess
import signal
import time
from web.module.splash_docker import DockerSplash
from web.settings import mitmproxy_port
from repoter_maker import make_report

PATH = os.path.dirname(os.path.abspath(__file__))
cmd = 'mitmdump -p ' + str(mitmproxy_port) + ' -s ' + PATH + '/../proxy_run.py'


class WebPipeline:
    def __init__(self):
        self.ds = DockerSplash(proxy_port=mitmproxy_port)
        self.ds.run()
        self.pid = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE).pid
        time.sleep(2)
        while True:
            if "running" != self.ds.splash_status():
                time.sleep(1)
            else:
                break

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        os.kill(self.pid, signal.SIGINT)
        self.ds.splash_close()
        make_report()
