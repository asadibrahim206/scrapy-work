import scrapy
# Use a relative import to avoid path issues
from ..items import UniversityItem 

class EbookSpider(scrapy.Spider):
    name = "uni"
    start_urls = ['https://www.chinesescholarshipcouncil.com/subject-wise-university-list-under-csc']

    def parse(self, response):
        # 1. Target the specific Computer Science section
        # We use 'following::table[1]' to get the table immediately after the CS header
        cs_table = response.xpath('//*[contains(text(), "Computer Science")]/following::table[1]')
        
        # 2. Iterate through rows, skipping the first (header) row
        for row in cs_table.xpath('.//tr[position() > 1]'):
            # Grab all text from table cells
            cells = row.xpath('.//td//text()').getall()
            
            for uni in cells:
                name = uni.strip()
                # Filter out numbers or empty strings
                if name and not name.isdigit():
                    item = UniversityItem()
                    item['university_name'] = name
                    yield 