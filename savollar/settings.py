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

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'savollar (+http://www.yourdomain.com)'
ITEM_PIPELINES = (
    'savollar.pipelines.savollarPipeline',
    # 'scrapyelasticsearch.ElasticSearchPipeline',
)

ONCURRENT_REQUESTS = 1000
ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = 9200
ELASTICSEARCH_INDEX = "savollar"

# ELASTICSEARCH_SERVER = 'localhost' # If not 'localhost' prepend 'http://'
# ELASTICSEARCH_PORT = 9200 # If port 80 leave blank
# ELASTICSEARCH_USERNAME = ''
# ELASTICSEARCH_PASSWORD = ''
# ELASTICSEARCH_INDEX = 'savollar'
# ELASTICSEARCH_TYPE = 'items'
# ELASTICSEARCH_UNIQ_KEY = 'url'
