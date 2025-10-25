import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebooks"

    start_urls = ["https://books.toscrape.com/"]