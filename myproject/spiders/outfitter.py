import scrapy

class OutfitterSpider(scrapy.Spider):
    name = "outfitter"
    start_urls = ["https://outfitters.com.pk/collections/men-t-shirts"]

    def parse(self, response):
        print("[PARSE]")
        items = response.xpath("//h3[@class='card__heading h5']/a")
        prices = response.xpath("//span[@class='money']/text()")
        
        for item in items:
            item = item.xpath("//h3[@class='card__heading h5']/a/text()")
            
            print(item)
            


          



    