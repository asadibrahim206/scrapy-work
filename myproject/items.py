# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy import Item,Field
from itemloaders.processors import MapCompose,TakeFirst
from scrapy.loader import ItemLoader


class ProductItem(scrapy.Item):
    title = Field()
    price = Field()
    
    
