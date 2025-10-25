import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebooks"

    start_urls = ["https://books.toscrape.com/"]

    def parse(self,response):
        print("[PARSE]")
        articles = response.css("article")
        for article in articles:
            item = article.css("h3 a::text").get()
            price = article.css(".price_color::text").get()
            print(item,price)
            yield{
                "item", item,
                "price", price
            }



    