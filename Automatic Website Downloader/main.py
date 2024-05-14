# Sources used: geeksforgeeks, stackoverflow
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import os
import tldextract
import pyautogui
pyautogui.FAILSAFE = False
folder = "Websites"
curr_dir = os.getcwd()
dir_path = os.path.join(curr_dir, folder)
print(dir_path)
# print(dir_path)
if not os.path.isdir(dir_path):
    os.makedirs(dir_path)
    print(f"Folder created with name: {folder}")

else:
    print(f"Folder already exists with name: {folder}")

path="chromedriver.exe"

# chrome_options = Options()
# chrome_options.add_argument("--headless")

with open('urls.txt', 'r', encoding='utf-8') as f:
        i = 1
        for line in f:
            url = 'https://' + line.strip()
            domain = tldextract.extract(url).domain
            file_name = str(i) + '_' + domain
            i+=1
            new_folder = os.path.join(curr_dir,folder,file_name)
            if not os.path.isdir(new_folder):
                os.makedirs(new_folder)
            print("Folder inside Websites folder is created: " + new_folder)
            full_path = dir_path+ "\\" +file_name+"\\"+file_name+".html"
            print(full_path)
            service = Service(executable_path=path)
            driver = webdriver.Chrome(service=service)
            driver.get(url)
            pyautogui.hotkey('ctrl','s')
            time.sleep(1)  
            pyautogui.typewrite(full_path)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            destination = "Websites"+"\\"+file_name+"\\"+file_name+".html"
            while not os.path.exists(destination) or os.path.getsize(destination) == 0:
                time.sleep(1)
            print(file_name+" Download complete!")


