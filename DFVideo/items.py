# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 所谓Item容器就是将在网页中获取的数据结构化保存的数据结构，类似于Python中字典

class DfvideoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_url = scrapy.Field()
    video_title = scrapy.Field()
    video_local_path = scrapy.Field()
