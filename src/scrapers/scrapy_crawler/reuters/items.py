import scrapy

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    summary = scrapy.Field()
    published = scrapy.Field()
    source = scrapy.Field()
