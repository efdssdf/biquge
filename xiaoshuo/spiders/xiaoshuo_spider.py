# coding=utf-8

import scrapy
import re
from xiaoshuo.items import CatalogItem,XiaoshuoItem

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjaGFubmVsX2lkIjoiMjcyNCIsInN1YiI6MzU3NjE4MzIxLCJpc3MiOiJodHRwOlwvXC93eDY4MTEzYTgyYzY2NTQwMjUueW91c2h1Z2UuY29tIiwiaWF0IjoxNTQzMjI3MDgyLCJleHAiOjE1NDM4MzE4ODIsIm5iZiI6MTU0MzIyNzA4MiwianRpIjoiTWdXUkFSN2l2OFBMVGxDTyJ9._-q-wCcPH3m8-Ymthwbj1scYdtyPu8G6kO28HwAJ7UQ"
headers = {'Origin': 'https://wx68113a82c6654025.youshuge.com'}

class QuotesSpider(scrapy.Spider):
    name = "xiaoshuo"

    def start_requests(self):
        global token
        global headers

        # yield scrapy.Request(url=url, callback=self.parse)
        l = [{"bookid":"17178","chapteid":"6143945","name":"妈咪枪手，爹地要趁早"},{"bookid":"16119","chapteid":"5746208","name":"幸孕宝贝：总裁爹地要给力"},{"bookid":"13339","chapteid":"4663751","name":"直播看见鬼"},{"bookid":"17247","chapteid":"6167229","name":"余生路上遇见你"},{"bookid":"3690","chapteid":"1534411","name":"甜心萌妻：总裁宠不停"},{"bookid":"17062","chapteid":"6112123","name":"爹地你别跑"},{"bookid":"3531","chapteid":"1463007","name":"总裁爹地宠上天"},{"bookid":"17360","chapteid":"6199851","name":"当你说爱我的时候"},{"bookid":"15671","chapteid":"5591869","name":"得说爱时必说爱"},{"bookid":"16765","chapteid":"5990676","name":"爱在心底口难开"}]
        for i in l:
            yield scrapy.FormRequest(
                url = "https://api.youshuge.com/getcontent",
                headers = headers,
                formdata = {"token":token,i["bookid"],i['chapteid']},
                meta = {"name":i["name"]}
                callback = self.parse
                )

    def parse(self, response):
        name = response.meta['name']
        d = eval(response.body.decode('unicode_escape').replace('\\','').replace('\r\n','').replace('""','"').replace('null','""'))
        content = d['data']['content'].replace('<p>','').replace('</p>','')
        res = "###"+d['data']['chapte_name']+"\r\n"+content+"\r\n"
        fiename = './'+name+'.txt'
        with open(fiename, 'a', encoding='utf-8') as f:
            f.write(res)
            if d['data']['next_chapte']:
                yield scrapy.FormRequest(
                    url = "https://api.youshuge.com/getcontent",
                    headers = headers,
                    formdata = {"token":token,"bookid":"17178",'chapteid':str(d['data']['next_chapte'])},
                    callback = self.parse
                    )
            else:
                fiename = './'+name+'.txt'
                with open(fiename, 'a', encoding='utf-8') as f:
                    f.write("###")