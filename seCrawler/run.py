from scrapy import cmdline
cmdline.execute("scrapy crawl keywordSpider -a keyword=Spider-Man -a se=baidu -a pages=10".split())