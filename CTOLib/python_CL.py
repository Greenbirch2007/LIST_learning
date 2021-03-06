#! -*- coding:utf-8 -*-



from lxml import etree
from selenium import webdriver
import pymysql
import datetime
import time
driver = webdriver.Chrome()






def get_one_page(url):
    driver.get(url)
    html = driver.page_source
    return html

# 不用遍历url取代翻页！


def parse_page(self,html):
    self.html = html
    seletor = etree.HTML(html)
    title = seletor.xpath('//*[@id="wrap"]/div[2]/div//div/div/div/div[1]/text()[1]')
    desc = seletor.xpath('//*[@id="wrap"]/div[2]/div//div/div/div/div[2]/text()[1]')
    link = seletor.xpath('//*[@id="wrap"]/div[2]/div//@href')
    for i1, i2,i3 in zip(title,desc, link):
        yield (i1,i2, 'https://www.ctolib.com' + i3)





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='list_learning',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into ctolib_python_links (title,DE,link) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass

url = 'https://www.ctolib.com/python/categoriesallsub.html'
html = get_one_page(url)
print(html)


# if __name__ == '__main__':
#     for offset in range(1,29):
#         url = 'https://www.jb51.net/list/list_5_' + str(offset) + '.htm'
#         html = get_one_page(url)
#         content = parse_page(html)
#         insertDB(content)
#         time.sleep(1)
#         print(datetime.datetime.now())








#
# create table ctolib_python_links(
#     id int not null primary key auto_increment,
# title varchar(50),
# DE varchar(88),
# link varchar(88)
# ) engine=Innodb  charset=utf8;
# #
# #
# drop table ctolib_python_links;
