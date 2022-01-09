import scrapy
from scrapy.http import Request
from bookprice.items import BookpriceItem
from bookprice.items import ImgData
import csv
import re


class BooksnuriaSpider(scrapy.Spider):
    name = 'booksNuria'
    allowed_domains = ['nuriakenya.com']
    start_urls = ['http://nuriakenya.com/']

    def start_requests(self):
        link_urls = ["https://nuriakenya.com/page/"+ format(i) + "/?s&post_type=product&product_cat=0" for i in range(1, 351)]
        for link_url in link_urls:
            print(link_url)
            request = Request(url=link_url, callback=self.parse_nuria_pages)
            yield request
        
    
    def parse_nuria_pages(self, response):
        item = BookpriceItem()
        contents = response.xpath('//li[starts-with(@class,"product-col ")]')
 
        for content in contents:
     
            
            item['BookTitle'] = content.xpath('.//h3[starts-with(@class, "woocommerce-loop-product__title")]/text()').extract_first()
            if item['BookTitle'] is not "":
                try:
                    item['BookAuthor'] = re.split(' by | BY: ', item['BookTitle'])[1].strip() 

                except:
               
                    item['BookAuthor'] = "N/A"
            item['BookPrice'] = content.xpath('.//span[starts-with(@class, "woocommerce-Price-amount amount")]/text()').extract_first()
            item['BookLink'] = content.xpath('.//div[starts-with(@class, "product-image")]/a/@href').extract_first()
            item['imageLink'] = content.xpath('.//img[contains(@class, "wp-post-image")]/@data-src').extract_first()
            item['BookStore'] = "NuriA kenya"
            
            
        yield item





    def parse(self, response):
        pass
