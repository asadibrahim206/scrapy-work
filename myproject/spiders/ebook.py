import scrapy

class EbookSpider(scrapy.Spider):
    name = "ebook"
    start_urls = ['https://www.chinesescholarshipcouncil.com/subject-wise-university-list-under-csc']

    def parse(self, response):
  
        # Based on your screenshot, it is: Top Universities for Computer Science and Technology
        cs_header = response.xpath('//*[contains(text(), "Computer Science")]')
        
        # Get the table that follows this header
        cs_table = cs_header.xpath('./following::table[1]')
        
        rows = cs_table.xpath('.//tr')
        
        for row in rows:
            # This table has two universities per row (column-1 and column-2)
            # We grab all text from all td cells in this row
            universities = row.xpath('.//td//text()').getall()
            
            for uni in universities:
                clean_name = uni.strip()
                if clean_name:
                    yield {
                        'university': clean_name
                    }
