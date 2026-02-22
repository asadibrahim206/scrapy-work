import scrapy

class OutfitterSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
       
        article = response.css("article.product_pod")
        for _ in article:
           title = article.css("h3 a::attr(title)").getall()
           price = article.css("div.product_price p.price_color::text").getall()

        
        yield{
            "title":title,
            "price":price
        }

        next_btn = response.css("li.next a::attr(href)").get()
        next_page = f"{self.start_urls[0]}/{next_btn}"
        print("Next Page :",next_page)

        
          



    