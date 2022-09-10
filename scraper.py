import requests

url = "https://www.bccondosandhomes.com/public/api2/search-listings"

payload = {
    "listing_status": "sold",
    "built_btw": [1900, 2022],
    "pricefrom": 0,
    "priceto": 20000000,
    "kitchens": "0+",
    "beds": "0+",
    "baths": "0+",
    "subareas": [],
    "types": [],
    "page": 1,
    "_token": "1goZFozMH7nPZ2A81Oi68lpKJCxERkP00OWysaT1"
}
headers = {
    "cookie": "intercom-id-mxuu7imk=6e0338b9-7303-4093-82c5-9bdd5305a255; intercom-session-mxuu7imk=; _ga=GA1.2.165702196.1662609956; _gid=GA1.2.1557892157.1662723935; _gat_gtag_UA_180666936_1=1; XSRF-TOKEN=eyJpdiI6ImVDXC9VZVM0Y3hBWUlzK0VIMGhLN0tRPT0iLCJ2YWx1ZSI6Iko0S05DcElJdE1YUWlrcEQ5d0xJN2xHeHY5WXNqeXl4VmFsc3FpZlkwaXNnd1FjVmZmRWlKUGJFYTFrRzVBQUciLCJtYWMiOiJiMzQwM2VjZTQ2MzY5ZDhjOWNkZjU5MTgzODUyNDYyNjUxOTAwYTIzOTgxMjc0ZjFmOThlMzVlMGUxZjg1OWNkIn0%3D; bccondosandhomes_session=eyJpdiI6IjFTNDZnNXBHcHE4VmRhVW1oalpXT3c9PSIsInZhbHVlIjoiamU1UnFvTUF3cjFoRzNhRFJralI3N0lRS0E1Y2RlcEgrKzFJY0JYNkErRTllclVKWlZsbytuSGhiZ3ArbW5OSiIsIm1hYyI6IjczNmI0NTQ4NTU0YTc5NmMwMzVhODhmZTdkMjdlYjRjNjkyMTMwNDQ5NzIxYWQzNjJhZTAyZWYwMzY5MWE0YjQifQ%3D%3D",
    "authority": "www.bccondosandhomes.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.bccondosandhomes.com",
    "referer": "https://www.bccondosandhomes.com/search-listings/?listing_status=sold",
    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "x-xsrf-token": "eyJpdiI6ImVDXC9VZVM0Y3hBWUlzK0VIMGhLN0tRPT0iLCJ2YWx1ZSI6Iko0S05DcElJdE1YUWlrcEQ5d0xJN2xHeHY5WXNqeXl4VmFsc3FpZlkwaXNnd1FjVmZmRWlKUGJFYTFrRzVBQUciLCJtYWMiOiJiMzQwM2VjZTQ2MzY5ZDhjOWNkZjU5MTgzODUyNDYyNjUxOTAwYTIzOTgxMjc0ZjFmOThlMzVlMGUxZjg1OWNkIn0="
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)