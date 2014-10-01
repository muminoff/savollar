# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from savollar.items import SavollarItem


class SavolspiderSpider(scrapy.Spider):
    name = "savolspider"
    allowed_domains = ["savollar.islom.uz"]
    # start_urls = (
    #     'http://www.savollar.islom.uz/',
    # )

    def start_requests(self):
        start_urls = ['http://savollar.islom.uz/page/%s' % i for i in xrange(1000)]
        return [scrapy.http.Request(url=start_url) for start_url in start_urls]

    def parse(self, response):
        hxs = scrapy.Selector(response)
        questions = hxs.xpath('//h2[@class=\'post-title\']')
        for q in questions:
            # item['id'] = str(uuid1())
            # item['link'] = q.xpath('a/@href').extract()[0]
            # item['desc'] = q.xpath('a/text()').extract()[0]
            link  = q.xpath('a/@href').extract()[0]
            # yield Request(url=item['link'], callback=self.printIt)
            yield Request(url=link, callback=self.getAnswer)

    def getAnswer(self, response):
        hxs = scrapy.Selector(response)
        item = SavollarItem()
        item['title'] = hxs.xpath('//section[@class=\'content\']//h1//text()').extract()[0]
        item['question'] = hxs.xpath('//section[@class=\'content\']//div[@class=\'entry-inner\']//p//text()').extract()[0]
        item['answer'] = hxs.xpath('//section[@class=\'content\']//article[@class=\'comment\']//div[@class=\'comment-content\']//text()').extract()[0]
        item['permalink'] = response.url
        yield item
