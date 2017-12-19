# encoding:utf-8

# from os import path
# from scrapy import signals
import json
from scrapy.exceptions import DropItem

import csv
import itertools


# from scrapy.xlib.pydispatch import dispatcher
# 把字段存入json文件中
class DataspiderPipeline(object):
    # def __init__(self):
    #     self.file = open("baiduSearch.json", 'w+', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     return item
    def __init__(self):
        self.csvwriter = csv.writer(open("baiduSearch.csv", "wb"), delimiter=',')
        self.csvwriter.writerow(['title', 'url', 'content', 'word'])

    def process_item(self, item, spider):
        rows = zip(item['title'], item['url'], item['content'], item['word'])
        for row in rows:
            self.csvwriter.writerow(row)
        return item

