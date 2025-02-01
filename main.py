#Created 30/01/2025
#Author Úna Cotter
#Scapper File test area

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service                

URL = "https://stats.beepbeep.ie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")  
chrome_options.add_argument("--disable-gpu")
ser = Service("chromedriver.exe")
service = webdriver.ChromeService(executable_path=chromedriver_bin)
driver = webdriver.Chrome(service=ser,options=chrome_options)
driver.get(URL)
print(driver.title)

#element = driver.find_element(By.ID ,"#Id_of_element")


page = requests.get(URL)
if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")
    print("Website Accessed Successfully.")
    results = soup.find(id = "sales-by-segment")
    #print(results.prettify())
else:
    print("Issue Accessing Website")