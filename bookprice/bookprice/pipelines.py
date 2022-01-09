# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookpricePipeline:
    def process_item(self, item, spider):
        return item

        
    def get_media_requests(self, item, info):
        adapter = ItemAdapter(item)
        for url in adapter['imageLink']:
            yield scrapy.Request(url)