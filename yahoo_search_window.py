from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def Yahoo_browser_start():
    browser = webdriver.Firefox()

    browser.get('http://www.yahoo.com')
    assert 'Yahoo' in browser.title

    elem = browser.find_element_by_name('p')  # Find the search box
    elem.send_keys('' + Keys.RETURN)

def search_end():
    browser.quit()

def headless_mode():    
    '''opts = Options()
    opts.set_headless()
    assert opts.headless  # Operating in headless mode
    browser = Firefox(options=opts)'''
    
    browser = webdriver.Firefox()
    browser.get('https://duckduckgo.com')
    elem=browser.find_element_by_name("search-wrap--home")
    elem.send_keys('duck'+ keys.RETURN)


def search_box(): 

    search_form = browser.find_element_by_id('search_form_input_homepage')
    search_form.send_keys('real python')
    search_form.submit()
    tracks = browser.find_elements_by_class_name('discover-item')
    assert(len(tracks) == 8)

def facebook_login():
    user = ""
    pwd = ""
    driver = webdriver.Firefox()
    driver.get("http://www.facebook.com")
    assert "Facebook" in driver.title
    elem = driver.find_element_by_id("email")
    elem.send_keys(user)
    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    driver.close()

facebook_login()





