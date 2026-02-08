import scrapy
from ..items import MyprojectItem
from scrapy.loader import ItemLoader


class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/catalogue/category/books/travel_2/"]
    
    def parse(self,response):
        
        ebooks = response.css("article")
        for ebook in ebooks:
            loader = ItemLoader(item=MyprojectItem(),selector=ebook)
            loader.add_css("title","h3 a::attr(title)")
            loader.add_css("price","p.price_color::text")
           
            yield loader.load_item()