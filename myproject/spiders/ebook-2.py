import scrapy

class OutfitterSpider(scrapy.Spider):
    name = "outfitter"
    start_urls = ["https://outfitters.com.pk/collections/men-t-shirts"]

    def parse(self, response):
        print("[PARSE]")
        # items = response.xpath("//h3[@class='card__heading h5']/a/text()").getall()
        # price = response.xpath("//span[@class='money']/text()").getall()

        shirts = response.xpath("//div[@class='card_information']")
        print(shirt)


        # yield {
        #         "item": items,
        #         "price": price
        #     }

       
             
            


          



    