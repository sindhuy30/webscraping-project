import scrapy
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            relative_url = book.css('h3 a').attrib['href']
            if 'catalogue/' in relative_url:
                book_url = 'https://books.toscrape.com/' + relative_url
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + relative_url
            yield scrapy.Request(book_url, callback=self.parse_book_page)

        next_page = response.css('li.next a ::attr(href)').get()
        if next_page:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self, response):
        product_main = response.css("div.product_main")
        if not product_main:
            self.logger.warning(f"No product_main found on {response.url}.")
            return

        table_rows = response.css("table tr")
        if len(table_rows) < 7:
            self.logger.warning(f"Not enough table rows on {response.url}.")
            return

        book_item = BookItem()
        book_item['url'] = response.url
        book_item['title'] = product_main.css("h1 ::text").get()
        book_item['upc'] = table_rows[0].css("td ::text").get()
        book_item['product_type'] = table_rows[1].css("td ::text").get()
        book_item['price_excl_tax'] = table_rows[2].css("td ::text").get()
        book_item['price_incl_tax'] = table_rows[3].css("td ::text").get()
        book_item['tax'] = table_rows[4].css("td ::text").get()
        book_item['availability'] = table_rows[5].css("td ::text").get()
        book_item['num_reviews'] = table_rows[6].css("td ::text").get()

        star_class = product_main.css("p.star-rating").attrib.get('class', '')
        book_item['stars'] = star_class

        book_item['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        ).get()

        desc = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        book_item['description'] = desc if desc else ""
        book_item['price'] = product_main.css('p.price_color ::text').get()

        if not book_item['title'] or not book_item['price']:
            self.logger.warning(f"Missing title/price: {response.url}")
            return

        yield book_item
