# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# 实现对item的处理，完成数据的查重、丢弃，验证item中数据，将得到的item数据保存等工作

class DfvideoPipeline:
    def process_item(self, item, spider):
        return item
