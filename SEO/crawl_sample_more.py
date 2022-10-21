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

### 上記URLから、指定したClassタグを取得
list_page = driver.find_elements_by_class_name("tF2Cxc")

### 抽出したタグからURLのリストをAタグで作成
url_list = []
for article in list_page:
    url = article.find_element_by_tag_name("a").get_attribute("href")
    ## print(article.text)
    url_list.append(url)

### 上記URLから、各ページに遷移してページタイトルを取得
title_list = []
for url in url_list:
    driver.get(url)
    time.sleep(3)

    title_list.append(driver.title)
print(title_list)
driver.quit()
