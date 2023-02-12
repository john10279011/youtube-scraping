import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.youtube.com/c/JohnWatsonRooney/videos'

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
details = []

driver.get(url)

items = driver.find_elements_by_xpath("//ytd-grid-video-renderer[contains(@class,'style-scope ytd-grid-renderer')]")
for item in items:
    name = item.find_element_by_xpath(".//a[contains(@class,'yt-simple-endpoint style-scope ytd-grid-video-renderer')]").text
    link = item.find_element_by_xpath(".//a[contains(@class,'yt-simple-endpoint style-scope ytd-grid-video-renderer')]").get_attribute('href')
    video = {
        'name':name,
        'link':link,
    }
    print(video)
    details.append(video)
    
df = pd.DataFrame(details)
# df.to_csv('youtube.csv',index=False)
driver.close()
print(df)