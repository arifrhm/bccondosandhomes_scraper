from playwright.sync_api import sync_playwright

url_api = ""
headers = {}
payload = {}

def on_request(request):
    global headers
    global url_api
    global payload

    if "api2" in request.url:
        payload = request.post_data_json
        url_api = request.url
        headers = request.headers

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    page.on("request", on_request)
    page.goto("https://www.bccondosandhomes.com/search-listings/",wait_until="networkidle")
    print(headers)
    print(payload)
    print(url_api)
    browser.close()
    
with sync_playwright() as playwright:
    run(playwright)

