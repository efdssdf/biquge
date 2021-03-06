# -*- coding: utf-8 -*-

import pymongo
from scrapy.conf import settings

class XiaoshuoPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        catalogname = settings["MONGODB_CATALOGNAME"]
        xiaoshuoname = settings["MONGODB_XIAOSHUONAME"]
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[catalogname]
        self.post1 = mydb[xiaoshuoname]

    def process_item(self, item, spider):
        data = dict(item)
        if isinstance(item, CatalogItem):
        	self.post.insert(data)
        elif isinstance(item, XiaoshuoItem):
        	self.post1.insert(data)
        return item

class CatalogPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_CATALOGNAME"]
        # 创建MONGODB数据库链接
        client = pymongo.MongoClient(host=host, port=port)
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])
        # 指定数据库
        mydb = client[dbname]
        # 存放数据的数据库表名
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item