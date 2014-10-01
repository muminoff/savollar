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
)

# CONCURRENT_REQUESTS = 1000
ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_INDEX = "savollar"
