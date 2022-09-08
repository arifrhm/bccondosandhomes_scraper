from datetime import datetime
import os
import re
from webbrowser import get
import requests
import json
from bs4 import BeautifulSoup
import time

# temp directory checking segment
current_dir = os.getcwd()

temp_dir = f'{current_dir}/temp'

print(f"Checking if {temp_dir} is available...")

if os.path.isdir(f"{temp_dir}"):
    print(f"{temp_dir} is available...")
else:
    print(f"{temp_dir} is not available!!!")
    print(f"Creating new directory {temp_dir}...")
    os.makedirs(f"{temp_dir}")
    print(f"Creating new directory {temp_dir} has been finished...")

URL_API = "https://www.bccondosandhomes.com/public/api2/search-listings"
URL_GET_ACTIVE = "https://www.bccondosandhomes.com/search-listings/"
URL_GET_SOLD = "https://www.bccondosandhomes.com/search-listings/?listing_status=sold"

payload_active = {
    "listing_status": "active",
    "built_btw": [
        1900,
        2022
    ],
    "pricefrom": 0,
    "priceto": 20000000,
    "kitchens": "0+",
    "beds": "0+",
    "baths": "0+",
    "subareas": [],
    "types": [],
    "page": 1,
    "_token": "9edb1e18508441d9ba2482277eae7183"
}
# payload_sold = {
#     "listing_status": "sold",
#     "built_btw": [
#         1900,
#         2022
#     ],
#     "pricefrom": 0,
#     "priceto": 20000000,
#     "kitchens": "0+",
#     "beds": "0+",
#     "baths": "0+",
#     "subareas": [],
#     "types": [],
#     "page": 1,
#     "_token": "1goZFozMH7nPZ2A81Oi68lpKJCxERkP00OWysaT1"
# }


def main(url):
    with requests.Session() as session:
        # Login segment
        print("Logging in...")
        # get_req = s.get(url_get)
        # p = session.post(url, data=payload_active)
        g = session.get(url)
        print("Sleep for 10 seconds")
        time.sleep(10)
        print("Wake up")
        print(g.text)


# #testing call file
if __name__ == "__main__":
    main("https://www.bccondosandhomes.com/search-listings/")