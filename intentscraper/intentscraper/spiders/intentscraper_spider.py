import sys
import scrapy

from intentscraper.items import IntentscraperItem


class DmozSpider(scrapy.Spider):
    name = "intentscraper"
    allowed_domains = ["*"]

    def __init__(self, *args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
        urls = kwargs.get('urls')
        self.start_urls = [urls]

    def parse(self, response):
        print sys.argv
        for sel in response.xpath('//ul/li'):
            item = IntentscraperItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

