from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a')

elem.click()
elems = browser.find_element_by_css_selector('p')
len(elems)

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()
browser.back()
browser.forward(browser.quit
browser.refresh)
