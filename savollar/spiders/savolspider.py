# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from savollar.items import SavolItem
from datetime import datetime


class SavolSpider(scrapy.Spider):
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
            yield Request(url=link, callback=self.get_answer)

    def get_answer(self, response):
        hxs = scrapy.Selector(response)
        item = SavolItem()
        item['title'] = hxs.xpath('//section[@class=\'content\']//h1//text()').extract()[0]
        item['question'] = '. '.join(t.strip() for t in hxs.xpath(
            '//section[@class=\'content\']//div[@class=\'entry-inner\']//p//text()'
        ).extract())
        item['answer'] = '. '.join(t.strip() for t in hxs.xpath(
            '//section[@class=\'content\']//article[@class=\'comment\']//div[@class=\'comment-content\']//text()').extract())
        item['author'] = hxs.xpath('//section[@class=\'content\']//p[@class=\'post-byline\']//a/text()').extract()[0].strip()
        item['permalink'] = response.url
        date_string = hxs.xpath('//section[@class=\'content\']//p[@class=\'post-byline\']//text()').extract()[1][3:]
        item['date'] = datetime.strptime(date_string, "%d/%m/%Y")
        yield item
