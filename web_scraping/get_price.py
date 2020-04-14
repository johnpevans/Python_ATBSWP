import bs4, requests

css_selector = '''body > div.page-slide > div.content-wrap > div > div >
div.item-wrap > div.item-block > div.item-tools > div > div.price-info-wrap >
div > div.price.item-price-wrap.hidden-xs.hidden-sm> span.sale-price'''

url = '''https://www.bookdepository.com/Automate-Boring-Stuff-With-Python-\
2nd-Edition-Al-Sweigart/9781593279929'''

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select(css_selector)
    return elems[0].text.strip()

price = getAmazonPrice(url)

print("The price is {0}".format(price))
