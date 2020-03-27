# -*- conding: utf-8 -*-
# @Time      :2020/3/10 17:24
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :try.py


# url = 'https://www.jianshu.com/p/d897d3422395'
# #xpath   //*[@id="__next"]/div[1]/div/div[1]/section[1]/article/div[1]/div[1]/div[2]/img


# for i in range(4):
#     print("i={}".format(i))
#     print('11111111111')
#     for j in range(4):
#         print("j={}".format(j))
#         print('22222222'+'\n')
#         if j ==2:
#             continue

import requests
from lxml import etree
import urllib.request
import urllib.parse
import time
# url_rooot= 'https://www.nature.com'
# url = 'https://www.nature.com/search?'

headers = {
'user-agent':
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'Connection':'close'
}

# headers = {
# 'user-agent':
#     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36',
# 'Connection':'close'
#
# }



# requests.adapters.DEFAULT_RETRIES = 5
# params ={'q':'Chunhai+Fan'}
#
# try:
#     r = requests.get(url, headers=headers, params=params).content
# except requests.exceptions.ConnectionError:
#
#     r.status_code = "Connection refused"
#
# index = etree.HTML(r)
# url = 'https://www.jianshu.com/p/d897d3422395'
url = 'https://www.nature.com/articles/s41467-020-14739-6/'
re = requests.get(url,headers=headers).text

html = etree.HTML(re)
print(html)

# paper_title = html.xpath('//*[@id="content"]/div/div/article/div[1]/div[1]/header/h1/text()')[0]
# print('获取论文标题')
# print(paper_title)


#//*[@id="figure-1"]/figure/div[1]/div[1]/a/picture/img
paper_title = html.xpath('//*[@id="figure-1"]/figure/div[1]/div[1]/a/picture/img/@src')[0]
# paper_title = html.xpath('//*[@id="indexCarousel"]/div/div/div/a/img/')
# paper_title = html.xpath('//*[@id="__next"]/div[1]/div/div[1]/section[1]/article/div[1]/div[1]/div[2]/img/@src')
# paper_title = html.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/article/p[2]/text()')
# paper_title = html.xpath('//*[@id="__next"]/div[1]/div/div[1]/section[1]/article/div[1]/div[1]/div[2]/img/@src')
print('获取论文标题')
print(paper_title)

filename = 'D:\PycharmProjects\Reptile\lunwen1.png'

paper_url = 'https:' + paper_title
print(paper_url)
# with open('D:\PycharmProjects\Reptile\pic\lunwen.png','wb',"a+",encoding='utf-8') as filename:
#     urllib.request.urlretrieve(url=paper_url,filename=filename)

urllib.request.urlretrieve(url=paper_url,filename=filename)



