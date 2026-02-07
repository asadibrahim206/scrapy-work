import scrapy
from ..items import MyprojectItem


class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]
    
    def parse(self,response):
        
        ebooks = response.css("article")
        for ebook in ebooks:
            project_item = MyprojectItem()
            items = MyprojectItem()
            items['title'] = ebook.css("a::text").get()
            items['price'] = ebook.css("p.price_color::text").get()
           
            yield items