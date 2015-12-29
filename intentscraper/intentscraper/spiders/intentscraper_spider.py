import re
import sys
import scrapy

from intentscraper.items import IntentscraperItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import BaseSpider, Spider
from urlparse import urljoin


class DmozSpider(CrawlSpider):
    name = "intentscraper"
    # allowed_domains = ["phpmongotweet-portalresearch.rhcloud.com"]
    # rules = (Rule(SgmlLinkExtractor(), callback='parse_items', follow=True),)
    # start_urls = ['http://phpmongotweet-portalresearch.rhcloud.com/']

    def __init__(self, *args, **kwargs):
        super(DmozSpider, self).__init__(*args, **kwargs)
        urls = kwargs.get('urls')
        domain = kwargs.get('domain')
        self.start_urls = [urls]
        self.allowed_domains = [domain]
        self.crawledLinks = []

    def parse(self, response):
        hxs = scrapy.Selector(response)
        links = hxs.xpath("//a/@href").extract()

        for n, i in enumerate(links):
            links[n]= urljoin(self.start_urls[0], i)

        linkPattern = re.compile("^(?:ftp|http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")
        print('A response from %s just arrived!' % response.url)
        for link in links:
            # If it is a proper link and is not checked yet, yield it to the Spider
            if linkPattern.match(link) and not link in self.crawledLinks:
                self.crawledLinks.append(link)
                yield scrapy.Request(link, callback = self.parse)

    def parse_category(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

