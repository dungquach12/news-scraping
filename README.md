# VnExpress News Scraper

Scrapy project for collecting articles from Kinh doanh topic [vnexpress.net/kinh-doanh](https://vnexpress.net/kinh-doanh).

## Features
- Crawls article pages
- Extracts title, time, author, number of comments, thumbnail, and URL.
- Saves results to JSONL and Excel via pipeline.

## Requirements
- Python 3.12
- Scrapy
- pandas
- openpyxl
- json

## Run:
```bash
scrapy crawl news
```

## Implement in future:
- Solve lazyloading issue, maybe change crawling tool
