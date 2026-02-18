from scrapy import Spider

class TrackerSpider(Spider):
    name = 'tracker'
    start_urls = ["https://www.redfin.com/city/9361/CA/Irvine"]

    def parse(self,response):
        print("our parse")
        response.css("h3 a")