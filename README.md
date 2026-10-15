# codewright_my: Python automation samples

## 1. web-scraper
Scrapes 100 book listings (title, price, rating, stock, link) from books.toscrape.com, a public practice site, and saves a sorted Excel file. Run: `python scraper.py`

## 2. excel-cleaner
Merges messy Excel files from several branches: it fixes column names, capitalises names, lowercases emails, turns "RM 1,200" into numbers, handles mixed date formats, drops blank rows and duplicates, and writes a report with a Totals sheet. Run: `python clean_merge.py`

Requirements: `pip install requests beautifulsoup4 pandas openpyxl`
