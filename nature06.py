import requests
from lxml import etree
import time
url_rooot= 'https://www.nature.com'
url = 'https://www.nature.com/search?'

headers = {
'user-agent':
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
'Connection':'close'

}
# requests.adapters.DEFAULT_RETRIES = 5
params ={'q':'Chunhai+Fan'}

try:
    r = requests.get(url, headers=headers, params=params).content
except requests.exceptions.ConnectionError:

    r.status_code = "Connection refused"

index = etree.HTML(r)
print(index)
paper_url = index.xpath('//div[@class="cleared"]/h2/a/@href')
#各个子页面链接
print(paper_url)
print('子链接长度为{}'.format(len(paper_url)))
#子页面地址
zilianjie = 0
for i  in paper_url:
    url_son = url_rooot+i

    # print("url_son的地址")
    # print(url_son)
    zilianjie +=1
    re = requests.get(url_son,headers=headers).text

    html = etree.HTML(re)
    with open("nature-blogs.docx","a+",encoding="utf-8") as file1:

        # 1.获取论文标题
        paper_title = html.xpath('//*[@id="content"]/div/div/article/div[1]/div[1]/header/h1/text()')[0]
        print('获取论文标题')
        print(paper_title)
        # 2.获取论文作者
        paper_author = html.xpath('string(//*[@id="content"]/div/div/article/div[1]/div[1]/header/ul[2])')
        print('获取论文作者')
        print(paper_author)
        # 3.获取Abstract
        paper_abstract = html.xpath('//*[@id="Abs1"]/text()')[0]
        print('获取Abstract')
        print(paper_abstract)
        # 4.获取Abstract内容
        paper_abstract_content = html.xpath('//*[@id="Abs1-content"]/p/text()')[0]
        print('获取Abstract内容')
        print(paper_abstract_content)

        # 5.获取Introduction
        sec_num = 1
        while 1:
            introduction_title = html.xpath('//*[@id="Sec{}"]/text()'.format(sec_num))
            if len(introduction_title) != 0:
                print('获取Introduction题目值是')
                print(introduction_title[0])

                # file0.write(introduction_title[0] + '\n')
                sec_concent=1

                while 1:
                    introduction_content = html.xpath('//*[@id="Sec{0}-content"]/p[{1}]/text()'.format(sec_num,sec_concent))
                    if len(introduction_content) != 0:
                        introduction_string = ""
                        for i in introduction_content:
                            introduction_string += i
                        print('获取sec{0}_content{1}的值是'.format(sec_num,sec_concent))
                        print(introduction_string)
                        sec_concent += 1



                        # with open('nature-blogs.docx','a+',encoding='utf-8') as  file:

                            # file0.write(paper_introduction[0]+'\n')
                            # # file.write(introduction_content[0]+'\n')
                            # file0.write(introduction_string+'\n')
                            # file0.write(i+'\n')
                            # file0.write('*'*50+'\n')
                    else:
                        break
                    continue
                sec_num += 1
            else:
                break


        #获取availability标题 //*[@id="data-availability"]
        # availability_title = html.xpath('//*[@id="data-availability"]/text()')
        # print('获取availability标题')
        # print(availability_title)
        #
        # #获取availability内容
        # availability_content = html.xpath('//*[@id="data-availability-content"]/p/text()')
        # print('获取availability_content')
        # print(availability_content)
        #
        # availability_string = ''
        # for i in availability_content:
        #     availability_string += i
        # print('availability_string所有内容')
        # print(availability_string)
        #
        #
        # #References //*[@id="Bib1"]
        # references_title = html.xpath('//*[@id="Bib1"]/text()')
        # print('获取references标题')
        # print(references_title)
        # ber = 0
        # cr = 'ref-CR'
        # while 1:
        #     ber +=1
        #     bra = str(ber)
        #     cr = 'ref-CR'+ bra
        #     print("cr为{}".format(cr))
        #
        #     references_content1 = html.xpath('//*[@id="{}"]/text()'.format(cr))
        #     if len(references_content1) != 0:
        #         print(references_content1)
        #         references_string = ''
        #         for i in references_content1:
        #             references_string += i
        #         print('references_string所有内容')
        #         print(references_string + '\n')
        #     else:
        #         break




    # print('获取references内容1')
    # print(references_content1)
    # #获取references内容1
    # references_content1 = html.xpath('//*[@id="ref-CR1"]/text()')
    # print('获取references内容1')
    # print(references_content1)
    #
    # references_string = ''
    # for i in references_content1:
    #     references_string += i
    # print('references_string所有内容')
    # print(references_string)
    #
    # # //*[@id="Bib1-content"]/div/ol/li[1]/ul  //*[@id="Bib1-content"]/div/ol/li[2]/ul
    # references_author1 = html.xpath('string(//*[@id="Bib1-content"]/div/ol/li[1]/ul)')
    # print('获取references作者1')
    # print(references_author1)
    #
    # #//*[@id="ref-CR2"]
    # references_content2 = html.xpath('//*[@id="ref-CR2"]/text()')
    # print('获取references内容2')
    # print(references_content2)
    #
    # references_string2 = ''
    # for i in references_content2:
    #     references_string2 += i
    # print('references_string2所有内容')
    # print(references_string2)

    # //*[@id="Bib1-content"]/div/ol/li[1]/ul
    # references_author1 = html.xpath('string(//*[@id="Bib1-content"]/div/ol/li[2]/ul)')
    # print('获取references作者1')
    # print(references_author1)



