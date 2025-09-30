import scrapy


class NewsscrapingItem(scrapy.Item):
    title = scrapy.Field()
    posted_time = scrapy.Field()
    author = scrapy.Field()
    number_of_comments = scrapy.Field()
    thumbnail_link = scrapy.Field()
    article_link = scrapy.Field()
