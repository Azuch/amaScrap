from playwright.sync_api import sync_playwright
import sys

def main():
    for link_index, link in enumerate(products):
        print(f"Scraping product {link_index + 1}/{len(products)}")
        try:
            title = scrape_product_title(page, link)
            print(title)
        except Exception as e:
            print(f"Error scraping product {link_index + 1}: {str(e)}")

def scrape_product_title(page, link):
    page.goto(link, wait_until='domcontentloaded')
    # Scroll to the end of the page
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(5000)  # Wait for 5 seconds after scrolling
    title_locator = page.locator("//span[@id='productTitle']")
    title = title_locator.inner_text()
    return title

if __name__ == "__main__":
    with open("list", "r") as f:
        products = f.readlines()

    products = [link.strip() for link in products if link.strip()]  # Remove empty lines

    if not products:
        print("No products found in the list")
        sys.exit()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        main()

