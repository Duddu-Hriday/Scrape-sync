from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
web="https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"
path="chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(web)
contents = driver.find_elements(by='xpath',value='//div[@class="text-wrapper style-scope ytd-video-renderer"]')


titles = []
channels = []
views = []
days = []



for content in contents:
    div_1 = content.find_element(by='xpath',value='.//div[@id="meta"]')
    div_2 = div_1.find_element(by='xpath',value='.//div[@id="title-wrapper"]')
    div_3 = div_2.find_element(by='xpath',value='.//h3[@class="title-and-badge style-scope ytd-video-renderer"]')
    div_4 = div_3.find_element(by='xpath',value='.//a[@id="video-title"]')
    div_5 = div_4.find_element(by='xpath',value='.//yt-formatted-string[@class="style-scope ytd-video-renderer"]')
    # title = div_5.text
    titles.append(div_5.text)
    # print(div_5.text)
    div_6 = div_1.find_element(by='xpath',value='.//ytd-video-meta-block[contains(@class,"style-scope ytd-video-renderer")]')
    div_7 = div_6.find_element(by='xpath',value='.//div[@id="metadata"]') # Will be used again
    div_8 = div_7.find_element(by='xpath',value='.//yt-formatted-string[@id="text"]')
    # channel = div_8.text
    channels.append(div_8.text)
    div_9 = div_7.find_element(by='xpath',value='.//div[@id="metadata-line"]')
    div_10 = div_9.find_elements(by='xpath',value='.//span[@class="inline-metadata-item style-scope ytd-video-meta-block"]')
    # print(div_10[1].text)
    views.append(div_10[0].text)
    days.append(div_10[1].text)
    # views = div_10[0].text
    # days = div_10[1].text

description = driver.find_elements(by='xpath',value="//yt-formatted-string[@id='description-text']")

info = []
for des in description:
    info.append(des.text)

data = {
        'Title of the Video': titles,
        'Channel Name': channels,
        'Views': views,
        'Released': days,
        'Description': info
        }

df = pd.DataFrame(data)
df.to_csv('youtube_trending.csv', index=False)

