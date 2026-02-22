import scrapy

class OutfitterSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[PARSE]")
        response.css("article.product_pod")
        
            


          



    