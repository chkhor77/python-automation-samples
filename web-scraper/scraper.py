"""Book listing scraper: collects title, price, rating and stock from
books.toscrape.com (a public practice site) into a clean Excel file."""
import requests, pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://books.toscrape.com/catalogue/page-{}.html"
RATING = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}

def scrape(pages=5):
    rows = []
    for p in range(1, pages + 1):
        url = BASE.format(p)
        soup = BeautifulSoup(requests.get(url, timeout=20).content, "html.parser")
        for b in soup.select("article.product_pod"):
            rows.append({
                "Title": b.h3.a["title"],
                "Price (GBP)": float(b.select_one(".price_color").text.strip().lstrip("Â£")),
                "Rating": RATING[b.p["class"][1]],
                "In Stock": "In stock" in b.select_one(".availability").text,
                "URL": urljoin(url, b.h3.a["href"]),
            })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    df = scrape()
    df.sort_values(["Rating", "Price (GBP)"], ascending=[False, True]).to_excel("books.xlsx", index=False)
    print(f"Saved {len(df)} books to books.xlsx")
