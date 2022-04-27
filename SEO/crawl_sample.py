from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

options = Options()
driver = webdriver.Chrome(".\chromedriver.exe", options=options)
## driver = webdriver.Chrome(options=options)

url = "https://www.google.com/search?q=旅行"
driver.get(url)
time.sleep(3)

### Put Elements Name from Source Code.
list_page = driver.find_elements_by_class_name("tF2Cxc")

for article in list_page:
    print(article.text)
driver.quit()
