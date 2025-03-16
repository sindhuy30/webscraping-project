# BookScraper

A **Scrapy** project designed to:

- **Crawl** [books.toscrape.com](https://books.toscrape.com/),  
- **Extract** book details (title, price, UPC, category, availability, etc.),  
- **Store** results in a **MySQL database** and an **Excel file**,  
- **Visualize** the extracted data using **Plotly** and **Pandas**.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation & Setup](#installation--setup)  


---

## Project Overview

**BookScraper** is a sample project built around Scrapy, a powerful Python framework for crawling and scraping websites. It collects structured data about books—such as title, category, price, availability, and rating—from the website [Books to Scrape](https://books.toscrape.com/).

The project demonstrates:

- **Crawling with Scrapy**  
- **Data cleaning/processing** with a custom pipeline (`BookscraperPipeline`)  
- **Storing results** in MySQL (`SaveToMySQLPipeline`) and Excel (`SaveToExcelPipeline`)  
- **Analyzing and visualizing** the scraped data with Pandas and Plotly  

---

## Features

1. **Scrapy Spider**  
   - Recursively follows pagination links.  
   - Extracts book data (e.g., title, UPC, price, category, description).

2. **Data Processing**  
   - Cleans strings (removing extra whitespace, stripping currency symbols).  
   - Converts prices/availability/reviews to numerical types.  
   - Maps star ratings (e.g., “one”, “two”, “five”) to integers.

3. **Multiple Data Pipelines**  
   - **MySQL**: Creates a `books` table (if it doesn’t exist) and inserts all data.  
   - **Excel**: Writes results to `books.xlsx`.

4. **Data Visualization**  
   - Generates **line**, **bar**, and **pie** charts based on the scraped data (using Plotly).  
   - **Line chart**: Average price by category.  
   - **Bar chart**: Book count by category.  
   - **Pie chart**: Distribution of book counts across categories.

---

## Prerequisites

You will need:

1. **Python 3.7+** (Any recent 3.x version is typically fine).  
2. **pip** (Python’s package manager).  
3. A local or remote **MySQL** server if you intend to store data in a MySQL database.  
4. Basic familiarity with command-line usage.

> **Windows Users**:  
> - Confirm that Python and pip are in your PATH.  
> - You may want to install [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) or [XAMPP](https://www.apachefriends.org/) for a local MySQL instance.

---

## Installation & Setup

1. **Clone or Download** this repository.  
2. **Navigate** into the project’s root folder (where `scrapy.cfg` is located).

3. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv

