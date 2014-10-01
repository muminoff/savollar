# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
from elasticsearch import Elasticsearch
from uuid import uuid1


class savollarPipeline(object):
    def process_item(self, item, spider):
        es = Elasticsearch([
            {"host": settings["ELASTICSEARCH_HOST"]},
        ])
        valid = True
        for data in item:
          # here we only check if the data is not null
          # but we could do any crazy validation we want
          if not data:

            raise DropItem("Missing %s of blogpost from %s" %(data, item['url']))
        if valid:
          es.index(
              index=settings["ELASTICSEARCH_INDEX"],
              doc_type="info",
              id=str(uuid1()),
              body=dict(item)
          )
          log.msg("Item indexed to ElasticSearch database %s:%s" %
                  (settings['ELASTICSEARCH_HOST'], settings['ELASTICSEARCH_PORT']),
                  level=log.DEBUG, spider=spider) 
        return item
