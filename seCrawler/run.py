from scrapy import cmdline
cmdline.execute("scrapy crawl keywordSpider -a keyword=农业数据联盟 -a se=baidu -a pages=1".split())