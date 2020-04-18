import bs4, requests

url = '''https://www.bookdepository.com/Automate-Boring-Stuff-With-\
Python-2nd-Edition-Al-Sweigart/9781593279929'''

browser = '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'''

headers = {'user-agent': browser}

css_selector = '''body > div.page-slide > div.content-wrap > div > div > \n
div.item-wrap > div.item-block > div.item-tools > div > div.price-info-wrap >\n
div > div.price.item-price-wrap.hidden-xs.hidden-sm > span.sale-price'''

res = requests.get(url, headers = headers)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select(css_selector)

print(elems[0].text)
