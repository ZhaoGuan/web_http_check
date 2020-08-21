# web_http_check
通过爬虫的方法检查页面资源加载情况


docker run -p 8050:8050 scrapinghub/splash


mitmdump -p 8899 -s proxy_run.py
 
scrapy crawl web
 
scrapy crawl web -a source=test

url_data.yml

login_url:
        boss: /admin/login.php
        boss1: /admin/login.php
        cms: /ken/login.php
user_data :
    test:
        boss:
            username: 392
            password: 123456
        boss1:
            username: 392
            password: 123456
        cms:
            username: 392
            password: 123456
host_data:
    test:
        boss: https://$$$$$$$$$$$$
        boss1: https://*******
        cms: https://********
url_data:
        boss:
            - /admin/mybook.html
            - /admin/u_userinfo_home.html?id=1798303
            - /1v1boss#/ClassBill/index?userid=1798303
            - /admin/deane_ducation.html#/DeanEducation
            - /admin/u_userinfo.html
            - /admin/u_student_list.html?tag_id=all&
        boss1:
            - /r_reserve2?user=1791256&times=
            - /s_user?user=1791256
            -  /s_teacher?teacher=373]
        cms:
          -  /
          - /teach_research/educational/series
          - /teach_research/label/list]
