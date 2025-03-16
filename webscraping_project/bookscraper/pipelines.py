import pandas
from itemadapter import ItemAdapter
import mysql.connector
import openpyxl

class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        for field_name in adapter.field_names():
            value = adapter.get(field_name)
            if field_name != 'description' and isinstance(value, str):
                adapter[field_name] = value.strip()
        for lowercase_key in ['category', 'product_type']:
            value = adapter.get(lowercase_key)
            if isinstance(value, str):
                adapter[lowercase_key] = value.lower()
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            if isinstance(value, str):
                value = value.replace('£', '').strip()
                try:
                    adapter[price_key] = float(value)
                except ValueError:
                    adapter[price_key] = 0.0
            else:
                adapter[price_key] = 0.0
        availability_string = adapter.get('availability', '')
        if '(' in availability_string:
            split_avail = availability_string.split('(')
            if len(split_avail) > 1:
                number_part = split_avail[1].split(' ')[0]
                try:
                    adapter['availability'] = int(number_part)
                except ValueError:
                    adapter['availability'] = 0
        else:
            adapter['availability'] = 0
        num_reviews_string = adapter.get('num_reviews', '')
        try:
            adapter['num_reviews'] = int(num_reviews_string)
        except:
            adapter['num_reviews'] = 0
        stars_string = adapter.get('stars', '')
        split_stars = stars_string.split()
        if len(split_stars) == 2:
            star_word = split_stars[1].lower()
            mapping = {
                "zero": 0, "one": 1, "two": 2,
                "three": 3, "four": 4, "five": 5
            }
            adapter['stars'] = mapping.get(star_word, 0)
        else:
            adapter['stars'] = 0
        return item

class SaveToMySQLPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  #Please replace with your password
            database='books'
        )
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INT NOT NULL AUTO_INCREMENT,
            url VARCHAR(255),
            title TEXT,
            upc VARCHAR(255),
            product_type VARCHAR(255),
            price_excl_tax DECIMAL(10,2),
            price_incl_tax DECIMAL(10,2),
            tax DECIMAL(10,2),
            price DECIMAL(10,2),
            availability INT,
            num_reviews INT,
            stars INT,
            category VARCHAR(255),
            description TEXT,
            PRIMARY KEY (id)
        )
        """)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.cur.execute("""
            INSERT INTO books (
                url, title, upc, product_type, price_excl_tax,
                price_incl_tax, tax, price, availability,
                num_reviews, stars, category, description
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            adapter.get("url"),
            adapter.get("title"),
            adapter.get("upc"),
            adapter.get("product_type"),
            adapter.get("price_excl_tax"),
            adapter.get("price_incl_tax"),
            adapter.get("tax"),
            adapter.get("price"),
            adapter.get("availability"),
            adapter.get("num_reviews"),
            adapter.get("stars"),
            adapter.get("category"),
            adapter.get("description"),
        ))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

class SaveToExcelPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = "Books"
        header = [
            "URL",
            "Title",
            "UPC",
            "Product_Type",
            "Price_Excl_Tax",
            "Price_Incl_Tax",
            "Tax",
            "Price",
            "Availability",
            "Num_Reviews",
            "Stars",
            "Category",
            "Description"
        ]
        self.ws.append(header)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        row = [
            adapter.get("url"),
            adapter.get("title"),
            adapter.get("upc"),
            adapter.get("product_type"),
            adapter.get("price_excl_tax"),
            adapter.get("price_incl_tax"),
            adapter.get("tax"),
            adapter.get("price"),
            adapter.get("availability"),
            adapter.get("num_reviews"),
            adapter.get("stars"),
            adapter.get("category"),
            adapter.get("description")
        ]
        self.ws.append(row)
        return item

    def close_spider(self, spider):
        self.wb.save("books.xlsx")
