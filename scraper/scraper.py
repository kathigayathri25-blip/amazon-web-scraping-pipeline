import time
import random
import os
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


SEARCH_QUERY = "laptops"

URL = f"https://www.amazon.in/s?k={SEARCH_QUERY}"


def scrape_amazon():

    print("Launching Browser...")

    options = webdriver.ChromeOptions()

    # Browser settings
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    # Fake browser headers
    options.add_argument(
        "user-agent=Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )

    # Launch Chrome
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    print("Opening Amazon...")

    driver.get(URL)

    # Wait for page loading
    time.sleep(random.randint(5, 8))

    print("Fetching page source...")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    all_products = soup.find_all(
        "div",
        {"data-component-type": "s-search-result"}
    )

    print("Products Found:", len(all_products))

    products = []

    for item in all_products:

        # Product Title
        try:
            title = item.h2.text.strip()
        except:
            title = None

        # Product Price
        try:
            price = item.find(
                "span",
                class_="a-price-whole"
            ).text.strip()
        except:
            price = None

        # Product Rating
        try:
            rating = item.find(
                "span",
                class_="a-icon-alt"
            ).text.strip()
        except:
            rating = None

        # Reviews Count
        try:
            reviews = item.find(
                "span",
                class_="a-size-base s-underline-text"
            ).text.strip()
        except:
            reviews = None

        products.append({
            "title": title,
            "price": price,
            "rating": rating,
            "reviews": reviews,
            "scraped_at": datetime.now()
        })

    # Convert to DataFrame
    df = pd.DataFrame(products)

    print("\nFirst 5 Products:\n")
    print(df.head())

    # Create folder
    os.makedirs("data/raw", exist_ok=True)

    # Save CSV
    output_file = "data/raw/amazon_raw_products.csv"

    df.to_csv(output_file, index=False)

    print(f"\nRaw data saved to: {output_file}")

    # Close browser
    driver.quit()

    print("\nScraping Completed Successfully")


if __name__ == "__main__":
    scrape_amazon()