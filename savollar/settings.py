# -*- coding: utf-8 -*-

# Scrapy settings for savollar project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'savollar'

SPIDER_MODULES = ['savollar.spiders']
NEWSPIDER_MODULE = 'savollar.spiders'

ITEM_PIPELINES = (
    'savollar.pipelines.CassandraExportPipleline',
    'savollar.pipelines.ElasticSearchIndexPipeline',
)

CONCURRENT_REQUESTS = 16
ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_INDEX = "savollar"

CASSANDRA_CLUSTER = ["localhost",]
CASSANDRA_KEYSPACE = "savollar"
