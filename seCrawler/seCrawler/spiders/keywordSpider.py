__author__ = 'Lilly'
from scrapy.spiders import Spider
from seCrawler.common.searResultPages import searResultPages
from seCrawler.common.searchEngines import SearchEngineResultSelectors
from seCrawler.common.searchEngines import SearchEngineTitleSelectors
from seCrawler.common.searchEngines import SearchEngineAbstractSelectors

from scrapy.selector import Selector
from seCrawler.items import KeywordspiderItem


class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com', 'google.com', 'baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None

    def __init__(self, keyword, se='bing', pages=50, *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        self.title = SearchEngineTitleSelectors[self.searchEngine]
        self.abstract = SearchEngineAbstractSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print("url:", url)
            self.start_urls.append(url)

    def parse(self, response):
        item = KeywordspiderItem()
        for url in Selector(response).xpath(self.selector).extract():
            # yield {'url':url}  不使用item，直接存储到txt文件中。
            item['url'] = url
            yield item
        # for title in Selector(response).xpath(self.title).extract():
        #     print("title:", title)
        for abstract in Selector(response).xpath(self.abstract).extract():
            print("abstract:", abstract)
        pass
