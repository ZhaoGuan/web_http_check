# web_http_check
通过爬虫的方法检查页面资源加载情况


docker run -p 8050:8050 scrapinghub/splash


mitmdump -p 8899 -s proxy_run.py
 
scrapy crawl web
 
scrapy crawl web -a source=test