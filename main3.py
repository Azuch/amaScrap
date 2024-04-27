from playwright.sync_api import sync_playwright
import sys

# Define custom headers
custom_headers = {
    "User-Agent": "Googlebot/2.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}

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
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            extra_http_headers=custom_headers,  # Set custom headers
            bypass_csp=True,  # Bypass Content Security Policy (CSP)
            ignore_https_errors=False,  # Handle HTTPS errors
            viewport={"width": 1280, "height": 720}  # Set viewport size
        )
        page = context.new_page()
        main()

