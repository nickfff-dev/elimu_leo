# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class BookpriceItem(scrapy.Item):
    BookIsbn = Field()
    BookTitle = Field()
    BookPrice = Field()
    BookAuthor = Field()
    BookPublisher = Field()

    imageLink = scrapy.Field()
    BookLink = Field()
    BookStore = scrapy.Field()

    
    pass


class ImgData(scrapy.Item):
    image_urls = Field()
    images = Field()