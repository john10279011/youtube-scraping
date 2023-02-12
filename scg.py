from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.youtube.com/c/JohnWatsonRooney/videos'

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get(url)

body = driver.find_element_by_css_selector('body')
body.click()
body.send_keys(Keys.PAGE_DOWN)