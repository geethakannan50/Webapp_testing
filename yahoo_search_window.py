from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def Yahoo_browser_start():
    browser = webdriver.Firefox()

    browser.get('http://www.yahoo.com')
    assert 'Yahoo' in browser.title

    elem = browser.find_element_by_name('p')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)

def search_end():
    browser.quit()

Yahoo_browser_start()
serch_end()




