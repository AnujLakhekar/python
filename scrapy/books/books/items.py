import scrapy

class BooksItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    img_url = scrapy.Field()