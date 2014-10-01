# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from savollar.items import SavollarItem


class SavolspiderSpider(scrapy.Spider):
    name = "savolspider"
    allowed_domains = ["savollar.islom.uz"]

    def start_requests(self):
        start_urls = ['http://savollar.islom.uz/page/%s' % i for i in xrange(1000)]
        return [scrapy.http.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        hxs = scrapy.Selector(response)
        questions = hxs.xpath('//h2[@class=\'post-title\']')
        for q in questions:
            link  = q.xpath('a/@href').extract()[0]
            yield Request(url=link, callback=self.getAnswer)

    def getAnswer(self, response):
        hxs = scrapy.Selector(response)
        item = SavollarItem()
        item['title'] = hxs.xpath('//section[@class=\'content\']//h1//text()').extract()[0]
        item['question'] = hxs.xpath('//section[@class=\'content\']//div[@class=\'entry-inner\']//p//text()').extract()[0]
        item['answer'] = hxs.xpath('//section[@class=\'content\']//article[@class=\'comment\']//div[@class=\'comment-content\']//text()').extract()[0]
        item['permalink'] = response.url
        yield item
