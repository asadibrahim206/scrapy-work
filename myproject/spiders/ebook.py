import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = {'https://books.toscrape.com/'}

    def parse(self, response):
        print("RESPONSE")
        ebooks= response.css("article.product-pod").extract()

        print(ebooks)
      