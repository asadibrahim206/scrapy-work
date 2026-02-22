import scrapy

class OutfitterSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[PARSE]")
        items = response.css("//h3[@class='card__heading h5']/a")
        prices = response.("//span[@class='money']/text()")
        
        for item in items:
            item = item.xpath("//h3[@class='card__heading h5']/a/text()")
            price = item.xpath("//html")
            print(item)
            print(price)
            


          



    