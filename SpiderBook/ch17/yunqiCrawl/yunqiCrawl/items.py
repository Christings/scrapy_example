# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YunqiBookListItem(scrapy.Item):
    novelId = scrapy.Field()  # 小说id
    novelName = scrapy.Field()  # 小说名称
    novelLink = scrapy.Field()  # 小说链接
    novelAuthor = scrapy.Field()  # 小说作者
    novelType = scrapy.Field()  # 小说类型
    novelStatus = scrapy.Field()  # 小说状态
    novelUpdateTime = scrapy.Field()  # 小说更新时间
    novelWords = scrapy.Field()  # 小说字数
    novelImageUrl = scrapy.Field()  # 小说封面


class YunqiBookDetailItem(scrapy.Item):
    novelId = scrapy.Field()  # 小说id
    novelLabel = scrapy.Field()  # 小说标签
    novelAllClick = scrapy.Field()  # 小说总点击量
    novelMonthClick = scrapy.Field()  # 小说月点击量
    novelWeekClick = scrapy.Field()  # 小说周点击量
    novelAllPopular = scrapy.Field()  # 小说总人气
    novelMonthPopular = scrapy.Field()  # 小说月人气
    novelWeekPopular = scrapy.Field()  # 小说周人气
    novelCommentNum = scrapy.Field()  # 小说评论数
    novelAllComm = scrapy.Field()  # 小说总推荐
    novelMonthComm = scrapy.Field()  # 小说月推荐
    novelWeekComm = scrapy.Field()  # 小说周推荐
