from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

options = Options()
## ChromedriverはWindowsで実行しています。Linux等の場合は適宜変更
driver = webdriver.Chrome(".\chromedriver.exe", options=options)
## driver = webdriver.Chrome(options=options)

## Keywordをファイルから読み出し
Keywords_list = pd.read_csv(".\Search_keyword.csv")
Keywords = Keywords_list["Keyword"]

df_list = []

for Keyword in Keywords:

 url = f"https://www.google.com/search?q={Keyword}"
 driver.get(url)
 time.sleep(2)
 
 ## Google検索を実行してリストページ毎にClassを取得
 list_page = driver.find_elements_by_class_name("tF2Cxc")
 
 url_list = []
 for article in list_page:
     url = article.find_element_by_tag_name("a").get_attribute("href")
     ## print(article.text)
     url_list.append(url)
 
 title_list = []
 text_num_list = []
 images_num_list = []
 h1_tag_list = []
 h1_tag_num_list = []
 h2_tag_list = []
 h2_tag_num_list = []

 for url in url_list:
     driver.get(url)
     time.sleep(2)
 
     title_list.append(driver.title)
 
     body = driver.find_element_by_tag_name("body").text
     text_num_list.append(len(body))
 
     images = driver.find_elements_by_tag_name("img")
     images_num_list.append(len(images))
 
     h1_list = driver.find_elements_by_tag_name("h1")
     h1_tag = []
     for h1 in  h1_list:
         h1_tag.append(h1.text)
     h1_tag_list.append(h1_tag)
     h1_tag_num_list.append(len(h1_tag))
 
 
     h2_list = driver.find_elements_by_tag_name("h2")
     h2_tag = []
     for h2 in  h2_list:
         h2_tag.append(h2.text)
     h2_tag_list.append(h2_tag)
     h2_tag_num_list.append(len(h2_tag))
 
 df = pd.DataFrame([title_list,text_num_list,images_num_list,h1_tag_list,h1_tag_num_list,h2_tag_list,h2_tag_num_list]).T
 df.columns = ["title","char_num","image_num","h1_list","h1_num","h2_list","h2_num"]
 df["index"] = df.reset_index()["index"] + 1
 df["Keyword"] = Keyword
 df_list.append(df)

df_all = pd.concat(df_list)
df_all.to_csv("Search_result.csv")
## print(title_list)
driver.quit()