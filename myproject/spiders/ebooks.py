import scrapy
from scrapy import Spider

class EbookSpider(scrapy.Spider):
    name = "ebook"
    starts_url = ["https://books.toscrape.com/"]
    def parse(self,response):
        print("SCRAPYYYYYYYYYYYYYYYYY")
        print(response)