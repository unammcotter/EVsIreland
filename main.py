#Created 30/01/2025
#Author Úna Cotter
#Scapper File test area

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service                
from selenium.webdriver.chrome.options import Options

url = "https://stats.beepbeep.ie/"

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")  
chrome_options.add_argument("--disable-gpu")

service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service)
#ser = Service("chromedriver.exe")
#driver = webdriver.Chrome(service=ser,options=chrome_options)
driver.get(url)
print(driver.title)

#element = driver.find_element(By.ID ,"#Id_of_element")


page = requests.get(url)
if page.status_code == 200:
    soup = BeautifulSoup(page.content, "html.parser")
    print("Website Accessed Successfully.")
    results = soup.find(id = "sales-by-segment")
    #print(results.prettify())
else:
    print("Issue Accessing Website")