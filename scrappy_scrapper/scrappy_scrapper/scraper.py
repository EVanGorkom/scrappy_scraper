import requests
from bs4 import BeautifulSoup
# from models import Item # This line is not working for some reason and will NOT import the models no matter the syntax. 
# More research needed...


url = "https://www.rei.com/s/mens-winter-clothing-accessories"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Use requests to get the HTML content of the page
response = requests.get(url, headers=headers)
html = BeautifulSoup(response.text, 'html.parser')  # Use BeautifulSoup for HTML parsing

def extract_text(element, selector):
  try:
    return element.select_one(selector).get_text(strip=True)
  except AttributeError:
    return None
  
items = []

# Use BeautifulSoup's CSS selector to find products
products = html.select("li.VcGDfKKy_dvNbxUqm29K")
for product in products: 
  item = {
  "name": extract_text(product, ".Xpx0MUGhB7jSm5UvK2EY"),
  "price": extract_text(product, "span[data-ui=sale-price]")
  }

  items.append(item)

for item in items:
  print(f'Name: {item["name"]}, Price: {item["price"]}')