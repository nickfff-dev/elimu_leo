import scrapy
from bookprice.items import BookpriceItem
from bookprice.items import ImgData
from scrapy.http import Request
import csv


class BookstbcSpider(scrapy.Spider):
    name = 'booksTbc'
    allowed_domains = ['textbookcentre.com']
    start_urls = ['http://textbookcentre.com/']

    def start_requests(self):
        with open("E:/books/bookprice/csvFiles/tbc.csv", "rU") as f:
            reader = csv.DictReader(f)
            for row in reader:
                url = row['url']
                link_urls = [url.format(i) for i in range(1, 77)]
                for link_url in link_urls:
                    print(link_url)
                    request = Request(url=link_url, callback=self.parse_product_pages)
               
                    yield request
                  
    def parse_product_link(self, response):
        item = BookpriceItem()
        item['BookTitle'] = response.xpath('/html/body/div[1]/main/div/div[3]/div/article/div[1]/div[2]/section/div[1]/h1/text()').extract_first()
        jwala =  response.xpath('/html/body/div[1]/main/div/div[3]/div/article/div[1]/div[2]/section/span[1]/text()').extract_first()
        if jwala is not None:
            item['BookIsbn'] = jwala.replace("ISBN:", "")                               
        item['BookAuthor'] = response.xpath('/html/body/div[1]/main/div/div[3]/div/article/div[1]/div[2]/section/p/a/text()').extract_first()
        item['BookPrice'] = response.xpath('/html/body/div[1]/main/div/div[3]/div/article/div[1]/div[3]/div/section/div/div[1]/div[1]/span/text()').extract_first()
        if item['BookPrice'] is not None:
            item['BookPrice'] = item['BookPrice'].replace("\n", "").strip()
        item['imageLink'] = "https://textbookcentre.com/"+response.xpath('/html/body/div[1]/main/div/div[3]/div/article/div[1]/div[1]/section/div[1]/div[1]/img[1]/@src').extract_first()
        item['BookLink'] = response.url
        item['BookStore'] = "Textbook Centre"
        if item['BookTitle'] is None:
            return
        yield item                         

    def parse_product_pages(self, response):
        item = BookpriceItem()
        content = response.xpath('/html/body/div[1]/main/div/div[3]/div/div[2]/div/section/div/div/div/a')
        for product_content in content:
            
            
            item['BookLink'] = "https://textbookcentre.com/" +product_content.xpath('./@href').extract_first()
    
            print(item['BookLink'])
         
            yield scrapy.Request(item['BookLink'], callback=self.parse_product_link)
            
            
            
            
    

    def parse(self, response):
        pass
