from playwright.sync_api import sync_playwright

from datetime import datetime
import sys

def main():
    for link_index, link in enumerate(products):
        page.goto(link, wait_until='domcontentloaded')
        page.wait_for_timeout(5_000)
        title_xpath = "//span[@id='productTitle']"
        print("Scraping product")
        title = page.locator(title_xpath).inner_text()
        print(title)

if __name__ == "__main__":
    with open("list", "r") as f:
        products = f.readlines()

    if len(products) == 0:
        print("No product found")
        sys.exit()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        main()
