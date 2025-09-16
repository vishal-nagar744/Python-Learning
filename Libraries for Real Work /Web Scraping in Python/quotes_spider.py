import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        # Next page follow
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)





# Real-Life Use Cases

# 🛒 E-commerce Price Tracking (Flipkart/Amazon products)
# 📰 News Scraping (headlines, articles)
# 📊 Job Data Extraction (LinkedIn, Indeed – legal issues dhyaan rakhna)
# 🎓 Research (Wikipedia, public datasets)


# ⚠️ Important Note:

# Scraping har site pe legal nahi hota. Always check robots.txt aur terms of service.
# Overloading servers avoid karo → use time.sleep() / Scrapy rate-limits.