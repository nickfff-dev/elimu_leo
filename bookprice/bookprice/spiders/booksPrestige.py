import scrapy
from scrapy.http import Request
from bookprice.items import BookpriceItem
from bookprice.items import ImgData
import re


class BooksprestigeSpider(scrapy.Spider):
    name = 'booksPrestige'
    allowed_domains = ['prestigebookshop.com']
    start_urls = ['http://prestigebookshop.com/']
    def start_requests(self):
        link_urls = ["https://prestigebookshop.com/page/"+ format(i) + "/?s=+&post_type=product"  for i in range(1, 244)]
        for link_url in link_urls:
            print(link_url)
            request = Request(url=link_url, callback=self.parse_prestige_pages, meta={'handle_httpstatus_list': [301]})
            yield request
    
    def parse_prestige_links(self, response):
        item = BookpriceItem()
        item['BookTitle'] = response.xpath('//h1[starts-with(@class, "product_title entry-title")]/text()').extract_first()
        item['BookAuthor'] = response.xpath('.//p[contains(text(), "Author:")]/text()').extract_first()
        if item['BookAuthor'] is not None:
            item['BookAuthor'] = item['BookAuthor'].replace('Author:', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\xa0', '').strip()
        item['BookPrice'] = response.xpath('//span[starts-with(@class, "woocommerce-Price-amount amount")]/text()').extract_first().replace('&nbsp', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\xa0', '')
        item['BookIsbn'] = response.xpath('.//p[contains(text(), "ISBN:")]/text()').extract_first()
        if item['BookIsbn'] is not None:
            item['BookIsbn'] = item['BookIsbn'].replace('ISBN:', '').replace('\n', '').replace('\r', '').replace('\t', '').replace('\xa0', '').strip()
        item['BookLink'] = response.url
        item['imageLink'] = response.xpath('//img[contains(@class, "wp-post-image")]/@data-src').extract_first()
        item['BookStore'] = "Prestige Bookshop"
        
        
        


        yield item

    def parse_prestige_pages(self, response):
        item = BookpriceItem()
        tents = response.xpath('//li[starts-with(@class,"product type-product post-")]')
        for tent in tents:
            
            item['BookLink'] = tent.xpath('.//a[contains(@class, "title")]/@href').extract_first()
            

            
            
            yield scrapy.Request(item['BookLink'], callback=self.parse_prestige_links)
          

    def parse(self, response):
        pass
