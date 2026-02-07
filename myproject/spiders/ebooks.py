import scrapy
from ..items import MyprojectItem


class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]
    
    def parse(self,response):
        print("[Parses]")
        ebooks = response.css("article")
        for ebook in ebooks:
            project_item = MyprojectItem()
            item = ebook.css("a::text").get()
            price = ebook.css("p.price_color::text").get()
           
            yield {
                "item": item,
                "price": price
            }