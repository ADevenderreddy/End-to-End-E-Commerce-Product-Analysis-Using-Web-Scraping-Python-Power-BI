import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.flipkart.com/search"
QUERY = "earphones"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}

all_data = []

for page in range(1, 11): 
    print(f"Scraping page {page}...")

    params = {
        "q": QUERY,
        "page": page
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("Blocked or failed, skipping page")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("div", class_="RGLWAk")

    for product in products:
        name_tag = product.find("a", class_="pIpigb")
        price_tag = product.find("div", class_="hZ3P6w")
        rating_tag = product.find("div", class_="MKiFS6")

        if name_tag and price_tag and rating_tag:
            all_data.append([
                name_tag.text.strip(),
                price_tag.text.strip(),
                rating_tag.text.strip()
            ])

    time.sleep(3)  

print("Total products scraped:", len(all_data))

df = pd.DataFrame(all_data, columns=["Name", "Price", "Rating"])
df["Price"] = df["Price"].str.replace("₹", "").str.replace(",", "").astype(int)
df["Rating"] = df["Rating"].astype(float)
df.to_csv("flipkart_earphones.csv", index=False)

