# coding=utf-8

import scrapy

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjaGFubmVsX2lkIjoiMjcyNCIsInN1YiI6MzU3NjE4MzIxLCJpc3MiOiJodHRwOlwvXC93eDY4MTEzYTgyYzY2NTQwMjUueW91c2h1Z2UuY29tIiwiaWF0IjoxNTQzMjI3MDgyLCJleHAiOjE1NDM4MzE4ODIsIm5iZiI6MTU0MzIyNzA4MiwianRpIjoiTWdXUkFSN2l2OFBMVGxDTyJ9._-q-wCcPH3m8-Ymthwbj1scYdtyPu8G6kO28HwAJ7UQ"
headers = {'Origin': 'https://wx68113a82c6654025.youshuge.com'}

class QuotesSpider(scrapy.Spider):
    name = "xiaoshuo"

    def start_requests(self):
        global token
        global headers

        # l = [{"bookid":"17178","chapteid":"6143945","name":"妈咪枪手，爹地要趁早"},{"bookid":"16119","chapteid":"5746208","name":"幸孕宝贝：总裁爹地要给力"},{"bookid":"13339","chapteid":"4663751","name":"直播看见鬼"},{"bookid":"17247","chapteid":"6167229","name":"余生路上遇见你"},{"bookid":"3690","chapteid":"1534411","name":"甜心萌妻：总裁宠不停"},{"bookid":"17062","chapteid":"6112123","name":"爹地你别跑"},{"bookid":"3531","chapteid":"1463007","name":"总裁爹地宠上天"},{"bookid":"17360","chapteid":"6199851","name":"当你说爱我的时候"},{"bookid":"15671","chapteid":"5591869","name":"得说爱时必说爱"},{"bookid":"16765","chapteid":"5990676","name":"爱在心底口难开"}]
        l = [{"bookid":"17178","chapteid":"6143945","name":"妈咪枪手，爹地要趁早"},{"bookid":"16119","chapteid":"5746208","name":"幸孕宝贝：总裁爹地要给力"},{"bookid":"13339","chapteid":"4663751","name":"直播看见鬼"},{"bookid":"17247","chapteid":"6167229","name":"余生路上遇见你"},{"bookid":"3690","chapteid":"1534411","name":"甜心萌妻：总裁宠不停"},{"bookid":"3531","chapteid":"1463007","name":"总裁爹地宠上天"},{"bookid":"16765","chapteid":"5990676","name":"爱在心底口难开"}]
        # l = [{"bookid":"15671","chapteid":"5591890","name":"得说爱时必说爱"}]
        for i in l:
            yield scrapy.FormRequest(
                url = "https://api.youshuge.com/getcontent",
                headers = headers,
                formdata = {"token":token,"bookid":i["bookid"],"chapteid":i['chapteid']},
                meta = {"name":i["name"]},
                callback = self.parse
                )

    def parse(self, response):
        name = response.meta["name"]
        d = eval(response.body.decode('unicode_escape').replace('\\','').replace('""','"').replace('null','""'))
        # print(d,'----------------------------d')
        content = d['data']['content'].replace('<p>','  ').replace('</p>','\r\n')
        res = "###"+d['data']['chapte_name']+"\r\n"+content+"\r\n"
        fiename = 'd:/xiaoshuos/youshuges/'+name+'.txt'
        # print(d['data']['next_chapte'],'-------------------------------next')
        if d['data']['next_chapte']:
            with open(fiename, 'a', encoding='utf-8') as f:
                f.write(res)
                yield scrapy.FormRequest(
                    url = "https://api.youshuge.com/getcontent",
                    headers = headers,
                    formdata = {"token":token,"bookid":str(d['data']['chapte']['book_id']),'chapteid':str(d['data']['next_chapte'])},
                    meta = {"name":name},
                    callback = self.parse
                    )
        else:
            fiename = 'd:/xiaoshuos/youshuges/'+name+'.txt'
            with open(fiename, 'a', encoding='utf-8') as f:
                f.write("###")