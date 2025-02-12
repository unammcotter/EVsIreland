#Created 30/01/2025
#Author Úna Cotter
#Scapper File test area

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service                
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import array as arr

def scrape_site (url, YR, MTH, car_make, ENGINE):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")  
    chrome_options.add_argument("--disable-gpu")

    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    #ser = Service("chromedriver.exe")
   
    #----------------------driver = webdriver.Chrome(service=ser,options=chrome_options)------------------------
    driver.get(url)
    sleep(2)
    print(driver.title)

    #access drop down filter menu
    #--------------------------------find & click on drowp down menu-----------------------------
    drop_arrow = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]')
    drop_arrow.click()
    #sleep(2)

    #-----------------------------------find & click on date menu---------------------------------------
    date_filter = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[2]/div/div[1]/div[1]/a')
    date_filter.click()
    #sleep(1)

    #find & click on year
    #select year
    year_element1 = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/select')
    year1 = Select(year_element1)
    year1.select_by_value(str(YR))
    #sleep(1)

    year_element2 = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/select')
    year2 = Select(year_element2)
    year2.select_by_value(str(YR))
    #sleep(1)

    #find & click on month
    #select start month
    month_element1 = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/select')
    month1 = Select(month_element1)
    month1.select_by_visible_text(MTH)
    #sleep(1)

    #select end month
    month_element2 = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/select')
    month2 = Select(month_element2)
    month2.select_by_visible_text(MTH)
    sleep(1)

    #----------------------find & click on vehicle menu----------------------------------------------
    veh_filter = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[2]/div/div[1]/div[3]/a')
    veh_filter.click()

    #find & select make
    make_element = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/input')
    make_element.send_keys("alfa romeo")
    sleep(2) #wait for search to load (wsl)
    make_element.send_keys(Keys.DOWN)
    make_element.send_keys(Keys.RETURN)
    make_element.send_keys(Keys.ESCAPE)  

    #find & select mmodel
    model_element = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/input')
    #model_element = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/input')))
    #sleep (10)
    model_element.send_keys("giulia")
    sleep(2)
    model_element.send_keys(Keys.DOWN)
    model_element.send_keys(Keys.RETURN)
    model_element.send_keys(Keys.ESCAPE)

#-------------------------------------------select engine type--------------------------------
    engine_element = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[5]/div/div[2]/input')
    #model_element = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/input')))
    #sleep (10)
    engine_element.send_keys("electric")
    sleep(2)
    engine_element.send_keys(Keys.DOWN)
    engine_element.send_keys(Keys.RETURN)
    engine_element.send_keys(Keys.ESCAPE)
    
    print("we got this far")
    sleep(10)

    filter_button = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[2]/a[1]')
    filter_button.click()

    sleep(10)


    #______________________________________________________________________________________________________


    #element = driver.find_element(By.ID ,"#Id_of_element")

    page = requests.get(url)
    #soup = BeautifulSoup(page.content, "html.parser")
    #segment = soup.find(id = "app.")
    #seg_element = driver.find_element(By.XPATH,'//*[@id="sales-by-segment"]/div[2]/div/div')
    seg_table = driver.find_element(By.XPATH,'//*[@id="sales-by-segment"]/div[2]/div/div/table')



    if not seg_table:
        print("Segment element not found")
    #print(results.prettify())

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        print("Website Accessed Successfully.")
        #results = soup.find(id = "sales-by-segment")
        #print(results.prettify())
    else:
        print("Issue Accessing Website")

    return

if __name__ == "__main__":
    url = "https://stats.beepbeep.ie/"

    YR = (2024,2023)
    #YR = (2024,2023,2022)

    MTH = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]

    #MTHnum = arr.array('i',[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    ENGINE = ["Electric", "Diesel Electric (Hybrid)", "Diesel/Plug-In Electric Hybrid",
            "Petrol Electric (Hybrid)", "Petrol/Plug-In Electric Hybrid"]

    car_make = ["ALFA ROMEO", "AUDI", "BENTLEY", "BMW", "BYD", "CITROEN", "CUPRA",
                "DACIA", "DS", "FERRARI", "FIAT", "FORD", "GWM", "HONDA", "HYUNDAI",
                "JAGUAR", "JEEP", "KIA", "LAND ROVE", "LEXUS", "LOTUS", "MAXUS",
                "MAZDA", "MERCEDES-BENZ", "MG", "MINI", "NISSAN", "OPEL", "PEUGEOT",
                "POLESTAR", "PORSCHE", "RENAULT", "SEAT", "SKODA", "SMART",
                "SSANGYONG", "SUBARU", "SUZUKI", "TESLA", "TOYOTA", "VOLKSWAGEN",
                "VOLVO"]
    for i in YR:
        for n in MTH:
            scrape_site(url, i, n, car_make, ENGINE)
            print("we did this")
