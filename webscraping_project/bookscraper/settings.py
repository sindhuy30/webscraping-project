BOT_NAME = "bookscraper"
SPIDER_MODULES = ["bookscraper.spiders"]
NEWSPIDER_MODULE = "bookscraper.spiders"

ROBOTSTXT_OBEY = True

SPIDER_MIDDLEWARES = {
   "bookscraper.middlewares.BookscraperSpiderMiddleware": 543,
}

DOWNLOADER_MIDDLEWARES = {
   "bookscraper.middlewares.BookscraperDownloaderMiddleware": 543,
}

ITEM_PIPELINES = {
   "bookscraper.pipelines.BookscraperPipeline": 300,
   "bookscraper.pipelines.SaveToMySQLPipeline": 400,
   "bookscraper.pipelines.SaveToExcelPipeline": 500,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
FEED_EXPORT_ENCODING = "utf-8"
