# Webscraping_Project

A **Scrapy** project designed to:

- **Crawl** [books.toscrape.com](https://books.toscrape.com/)  
- **Extract** book details (title, price, UPC, category, availability, etc.)  
- **Store** results in a **MySQL database** and an **Excel file**  
- **Visualize** the extracted data using **Plotly** and **Pandas**

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Installation & Setup](#installation--setup)  
5. [Usage](#usage)  
6. [Troubleshooting](#troubleshooting)  
7. [License](#license)

---

## Project Overview

**Webscraping_Project** is a powerful data scraping solution built using **Scrapy**. This project extracts structured book data — including titles, prices, categories, and availability — from the website [Books to Scrape](https://books.toscrape.com/).

The project demonstrates:

- **Efficient Crawling** using Scrapy's recursive spider functionality.  
- **Data Cleaning** and processing with custom pipelines.  
- **Data Storage** via MySQL (`SaveToMySQLPipeline`) and Excel (`SaveToExcelPipeline`).  
- **Data Visualization** for insights and analysis using Plotly and Pandas.

---

## Features

1. **Scrapy Spider**  
   - Recursively follows pagination links.  
   - Extracts essential book data (title, price, category, etc.).

2. **Data Processing Pipelines**  
   - **Cleans** and formats data (e.g., removes currency symbols, converts text to numbers).  
   - Maps star ratings (e.g., "one", "two", etc.) to integers for easier analysis.

3. **Data Storage**  
   - **MySQL Pipeline**: Automatically creates a `books` table and inserts records.  
   - **Excel Pipeline**: Saves data in `books.xlsx`.

4. **Data Visualization**  
   - **Line Chart**: Average book price by category.  
   - **Bar Chart**: Book count by category.  
   - **Pie Chart**: Distribution of books by category.

---

## Prerequisites

1. **Python 3.7+** (Any recent 3.x version should work).  
2. **pip** (Python’s package manager).  
3. **MySQL Server** for database storage.  
4. Basic knowledge of Python and command-line usage.

---

## Installation & Setup

1. **Clone or Download** this repository:  
   ```bash
   git clone https://github.com/your-username/webscraping_project.git
Navigate into the project folder:

bash
Copy
Edit
cd webscraping_project
Create a Virtual Environment (recommended):

bash
Copy
Edit
python -m venv venv
Activate the Virtual Environment:

On Windows:
bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure MySQL (Optional for Excel-only storage):

In pipelines.py, update the credentials in SaveToMySQLPipeline:
python
Copy
Edit
self.conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='books'
)
Usage
1. Run the Scraper
Activate your virtual environment, then run:

bash
Copy
Edit
scrapy crawl bookspider
2. Data Storage
The spider will automatically:
Store book data in MySQL.
Save book data in books.xlsx.
3. Run Data Visualization
After scraping completes, run the visualization script:

bash
Copy
Edit
python analysis/data_visualization.py
4. Visualizations
Line Chart: Average book price by category.
Bar Chart: Book count by category.
Pie Chart: Distribution of books by category.
Troubleshooting
Common Issues & Solutions

MySQL Connection Error:

Ensure MySQL server is running.
Verify your MySQL credentials in pipelines.py.
File Not Found (books.xlsx):

Confirm the spider successfully scraped data.
Ensure the SaveToExcelPipeline is properly configured.
Module Not Found Error:

Ensure you activated the virtual environment (venv).
Reinstall dependencies: pip install -r requirements.txt.

License
This project is licensed under the MIT License.
Feel free to modify, distribute, or improve this project for educational and commercial use.
