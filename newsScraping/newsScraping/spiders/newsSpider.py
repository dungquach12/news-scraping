import scrapy
from ..items import NewsscrapingItem

class CountriesSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        "https://vnexpress.net/kinh-doanh",
    ]

    def parse(self, response):
        article_links = response.css("article[class*='item-news'] a::attr(href)").getall()
        for article_link in article_links:
            yield response.follow(article_link, self.parse_article)

        next_page = response.css('a.btn-page.next-page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        yield NewsscrapingItem(
            title = response.css("h1.title-detail::text").get(),
            posted_time = response.css("span.date::text").get(),
            author = response.xpath('//span[@id="article-end"]/preceding-sibling::p[1]/strong/text()').get(),
            number_of_comments = response.css("label#total_comments::text").get() or "0",
            thumbnail_link = response.css("meta[property='og:image']::attr(content)").get(),
            article_link = response.url,
        )

    