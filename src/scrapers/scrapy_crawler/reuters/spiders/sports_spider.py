import scrapy
from scrapy import Request
from reuters.items import ArticleItem
from dateutil import parser


class SportsSpider(scrapy.Spider):
    name = "sports"
    allowed_domains = ["aljazeera.com"]
    start_urls = ["https://www.aljazeera.com/sports/"]

    def parse(self, response):
        article_links = response.css('a[href^="/sports/"]::attr(href)').getall()
        full_links = [
            response.urljoin(link)
            for link in set(article_links)
            if not link.startswith("/sports/live")
        ]
        self.logger.info(f"🔗 Found {len(full_links)} article links")

        for link in full_links:
            yield Request(url=link, callback=self.parse_article)

    def parse_article(self, response):
        item = ArticleItem()

        item["title"] = response.css("h1::text").get()
        item["link"] = response.url
        item["source"] = "Al Jazeera Sports"
        item["author"] = response.css('[class*="author-name"]::text').get()

        datetime_str = response.css("time::attr(datetime)").get()
        if datetime_str:
            try:
                item["published"] = parser.parse(datetime_str)
            except Exception as e:
                self.logger.warning(f"⚠️ Could not parse date: {datetime_str} ({e})")
                item["published"] = None
        else:
            item["published"] = None

        paragraphs = response.css("article p::text").getall()
        summary = " ".join(paragraphs).strip()
        item["summary"] = summary[:300] if summary else ""

        yield item
