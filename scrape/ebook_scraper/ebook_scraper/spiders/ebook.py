import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls =["https://books.toscrape.com/"]

    def parse(self,response):
        print("[----------OUR RESPONSE----------]")
        ebooks = response.css("article.product_pod")

        for ebook in ebooks:
            # title = ebook.css("h3 a::attr(title)").get()
              title = ebook.css("h3 a").attrib['title']
              price = ebook.css("p.price_color::text").get()

              yield{
                   "title":title, "price":price
              }   