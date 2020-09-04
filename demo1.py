#@Time:2020/9/3 17:06
#@Author:chenlou c00452131
#@File:demo1.py

import requests
from lxml import html
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
def index():
    for num in range(1,50,1):
        try:
            base_url='https://www.3dmgame.com/original_40_{0}/'.format(num)
            response=requests.get(base_url,headers=headers)
            # print(response.status_code)
            print(base_url+'访问成功')
            response.encoding=('utf-8')
        except:
            print("error")
        html=response.text
        clean(html)
def clean(html):
    #代码预处理
    html=html.etree.HTML(html)
    #html=html.etree(html)
    # print(html)
    #xpath守则
    game_name=html.xpath("//div[@class='bt']/a/text()")
    game_score=html.xpath("//a[@class='font']/text()")
    test_time=html.xpath("//div[@class='time']/text()")
    short_list=html.xpath("//div[@class='p']/p/text()")
    # hot_index=html.xpath("//span[@class='selectarcnum']/text()")
    # print(game_score)
    # print(game_score)
    # print(test_time)
    for name,score,time ,list in zip(game_name,game_score,test_time,short_list):
        #提取游戏名称
        name=name.split('》')[0]
        name=name+'》'
        #游戏单体信息加工
        info=name+'  3dm评分：'+score+'\n\t\t3dm评测时间：'+time+'\n\t\t简介：'+list+'\n'
        # print(info)
        #保存信息
        sto(info)
def sto(info):
    fp.write(info)
if __name__ == '__main__':
    fp=open('./3dm游戏评测.txt','a',encoding='utf-8')
    index()
    fp.close()