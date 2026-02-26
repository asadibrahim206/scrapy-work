import scrapy
from ..items import ProductItem

class OutfitterSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://priceoye.pk/laptops"]

    def parse(self, response):
        # Correctly selecting the product containers
        details = response.css(".detail-box")
        
        for product in details:
            item = ProductItem()
            

            raw_title = product.css("h4.p-title::text").get()
            
          
            raw_price = product.css(".price-diff-retail span::text").re_first(r'[0-9,]+')

            item['title'] = raw_title.strip() if raw_title else None
            item['price'] = raw_price

            yield 

        
        
        
          



    