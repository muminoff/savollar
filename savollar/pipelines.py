# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don"t forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log
from elasticsearch import Elasticsearch
from uuid import uuid1
from cqlengine.connection import setup
from savollar.models import SavolModel


class ElasticSearchIndexPipeline(object):
    def process_item(self, item, spider):
        es = Elasticsearch([
            {"host": settings["ELASTICSEARCH_HOST"]},
        ])
        valid = True
        for data in item:
            if not data:
                raise DropItem("Missing %s of item from %s" %(data, item["link"]))

        if valid:
            es.index(
                index=settings["ELASTICSEARCH_INDEX"],
                doc_type="info",
                id=str(uuid1()),
                body=dict(item)
            )
            log.msg("Item indexed to ElasticSearch database %s:%s" %
                    (settings["ELASTICSEARCH_HOST"], settings["ELASTICSEARCH_PORT"]),
                    level=log.DEBUG, spider=spider) 
        return item


class CassandraExportPipleline(object):
    def process_item(self, item, spider):
        print ">>>>>>>>>>>>>>>", item
        setup(settings["CASSANDRA_CLUSTER"], settings["CASSANDRA_KEYSPACE"])
        valid = True
        for data in item:
            if not data:
                raise DropItem("Missing %s of item from %s" %(data, item["link"]))

        if valid:
            model = SavolModel()
            model.title = item["title"]
            model.question = item["question"]
            model.answer = item["answer"]
            model.author = item["author"]
            model.permalink = item["permalink"]
            model.date = item["date"]
            model.tags = item["title"].split()
            model.save()
            log.msg("Item exported to Cassandra database %s/%s" %
                    (settings["CASSANDRA_HOST"], settings["CASSANDRA_KEYSPACE"]),
                    level=log.DEBUG, spider=spider) 
        return item
