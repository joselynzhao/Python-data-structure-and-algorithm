#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:pachong3.py
@TIME:2020/7/31 17:01
@DES:
'''
import time
from bs4 import BeautifulSoup  # 处理抓到的页面
import sys
import requests
import re
import importlib

importlib.reload(sys)  # 编码转换，python3默认utf-8,一般不用加

# ff = open('test.txt', 'w')

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}  # 定义头文件

ff = open('result.txt','w')
def getfromBaidu():
    start = time.clock()
    global order
    order  = 0
    for k in range(1, 50):
        geturl(k)
    end = time.clock()
    print(end - start)


def geturl(k):
    number = str((k - 1) * 10)
    path = 'https://www.baidu.com/s?wd=%E6%B6%82%E4%BA%9A%E5%BA%86&pn='+number+'&oq=%E6%B6%82%E4%BA%9A%E5%BA%86&ie=utf-8&usm=1&rsv_pq=cfb1f9ec00028b62&rsv_t=1bf8iGvhHo%2FmOTo4xluWlPdIN4Nnp1CaUvtAHCfY%2F2RIoqOECLttdDT5xqU&rsv_page=1'
    # path = 'https://www.baidu.com/s?wd=%E5%92%96%E5%95%A1&pn=' + number + '&oq=%E5%92%96%E5%95%A1&ie=utf-8&usm=1&rsv_pq=9ccd7f6500120ebb&rsv_t=d92fDeHr8TAXzN%2FuqzNW3xd3BcU3lunThKY2lkUUobFc3Ihjx46MPW4iNbc'
    # print(path)
    content = requests.get(path, headers=headers)
    # 使用BeautifulSoup解析html
    soup = BeautifulSoup(content.text, 'html.parser')

    tagh3 = soup.find_all('div', {'class', 'result c-container '})
    # print(tagh3)

    for h3 in tagh3:
        try:
            global order
            order +=1
            title = h3.find(name="h3", attrs={"class": re.compile("t")}).find('a').text.replace("\"", "")
            print(title)
            # print(n)
            ff.write('\n'+str(order)+'~ ')
            ff.write(title+' ~ ')
        except:
            title = ' ~ '

        try:
            url = h3.find(name="a", attrs={"class": re.compile("c-showurl")}).get('href')
            print(url + '\n')
            ff.write(url+' ~ ')
            # print('\n')
        except:
            url = ' ~ '
        try:
            abstract = h3.find(name="div", attrs={"class": re.compile("c-abstract")}).text.replace("\"", "")
            print(abstract)
            ff.write(abstract)
        except:
            abstract = ''

        # ff.write('\n')


if __name__ == '__main__':
    getfromBaidu()
    ff.close()