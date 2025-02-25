#Created 30/01/2025
#Author Úna Cotter
#Scapper File test area
#To do:
#Change variable to hnadle table
#need to erase alfero and replace with audi
#save table as an excel file

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
import string
#from csv import writer
import csv
import pandas as pd

def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")  
    chrome_options.add_argument("--disable-gpu")

    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)

    return driver

def drop_down_menu (url, driver):
    #----------------------driver = webdriver.Chrome(service=ser,options=chrome_options)------------------------
    driver.get(url)
    sleep(1)
    print(driver.title)

    #access drop down filter menu
    #--------------------------------find & click on drowp down menu-----------------------------
    drop_arrow = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]')
    drop_arrow.click()

    #-----------------------------------find & click on date menu---------------------------------------
    date_filter = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[2]/div/div[1]/div[1]/a')
    date_filter.click()

    #----------------------find & click on vehicle menu----------------------------------------------
    veh_filter = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[2]/div/div[1]/div[3]/a')
    veh_filter.click()

def enter_yr_mth(driver,YR,MTH):
    #find & click on year
    #select year
    year_element1 = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/select')
    year1 = Select(year_element1)
    year1.select_by_value(str(YR))

    year_element2 = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/select')
    year2 = Select(year_element2)
    year2.select_by_value(str(YR))

    #find & click on month
    #select start month
    month_element1 = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/select')
    month1 = Select(month_element1)
    month1.select_by_visible_text(MTH)

    #select end month
    month_element2 = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/select')
    month2 = Select(month_element2)
    month2.select_by_visible_text(MTH)
    sleep(1)

def enter_make(driver,car_make):
    #find & select make
    make_element = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/input')
    #make_element.send_keys("MERCEDES-BENZ"
    make_element.send_keys(Keys.BACK_SPACE)
    sleep(1)
    make_element.send_keys(car_make)
    sleep(1) #wait for search to load (wsl)
    make_element.send_keys(Keys.DOWN)
    make_element.send_keys(Keys.RETURN)
    make_element.send_keys(Keys.ESCAPE) 

def enter_engine(driver,engine):
    #-------------------------------------------select engine type--------------------------------
    engine_element = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[5]/div/div[2]/input')
    #engine_element = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[5]/div/div[2]/input')))
    #sleep (10)
    #engine_element.send_keys("electric")
    engine_element.send_keys(Keys.BACK_SPACE)
    engine_element.send_keys(engine)
    sleep(1)
    engine_element.send_keys(Keys.DOWN)
    engine_element.send_keys(Keys.RETURN)
    engine_element.send_keys(Keys.ESCAPE)     

def click_filter_button(driver):
    filter_button = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[2]/a[1]')
    filter_button.click()
    sleep(5)

def enter_model(driver,car_model):
    #find & select mmodel
    model_element = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/input')
    model_element = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/input')))
    model_element.send_keys(Keys.BACK_SPACE)
    sleep (1)
    model_element.send_keys(car_model)
    sleep(2)
    model_element.send_keys(Keys.DOWN)
    model_element.send_keys(Keys.RETURN)
    model_element.send_keys(Keys.ESCAPE)

def get_models(driver):
    #-------------------------------find avaible models---------------------------------------
    car_model_element = driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[5]/div/div[2]/div/div/table/tbody/tr')
    rows = len(driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[5]/div/div[2]/div/div/table/tbody/tr'))
    cols = len(driver.find_elements(By.XPATH, '//*[@id="sales-by-model"]/div[2]/div/div/table/tbody/tr[1]/td'))
    print(rows) 
    print(cols) 

    car_models = [None] * rows

    if rows != 0:
        for r in range(1, rows+1): 
            # obtaining the text from each column of the table 
            car_models[r-1] = driver.find_element(By.XPATH, '//*[@id="sales-by-model"]/div[2]/div/div/table/tbody/tr['+str(r)+']/td['+str(4)+']').text
            car_models[r-1] = car_models[r-1].lower()
    
    return car_models

def get_seg(driver):
    seg_element = driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[6]/div/div[2]/div/div/table/tbody/tr')
    rows = len(driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[6]/div/div[2]/div/div/table/tbody/tr'))
    cols = len(driver.find_elements(By.XPATH, '/html/body/div/div[3]/div/div[2]/div[6]/div/div[2]/div/div/table/tbody/tr[1]/td'))
    print(rows) 
    print(cols)

    seg = [None] * rows

    if rows != 0:
        for r in range(1, rows+1): 
            # obtaining the text from each column of the table 
            seg[r-1] = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[2]/div[6]/div/div[2]/div/div/table/tbody/tr['+str(r)+']/td['+str(3)+']').text
            #seg[r-1] = seg[r-1].lower()
    
    return seg

def get_body(driver):
    body_element = driver.find_elements(By.XPATH,'//*[@id="sales-by-body-type"]/div[2]/div/div/table/tbody/tr')
    rows = len(driver.find_elements(By.XPATH,'//*[@id="sales-by-body-type"]/div[2]/div/div/table/tbody/tr'))
    cols = len(driver.find_elements(By.XPATH, '//*[@id="sales-by-body-type"]/div[2]/div/div/table/tbody/tr[1]/td'))
    print(rows) 
    print(cols)

    body= [None] * rows

    if rows != 0:
        for r in range(1, rows+1): 
            # obtaining the text from each column of the table 
            body[r-1] = driver.find_element(By.XPATH, '//*[@id="sales-by-body-type"]/div[2]/div/div/table/tbody/tr['+str(r)+']/td['+str(2)+']').text
            #body[r-1] = body[r-1].lower()
    
    return body

def enter_body(driver,car_body):
    #find & select make
    body_element = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[3]/div/div[2]/input')
    #make_element.send_keys("MERCEDES-BENZ")
    body_element.send_keys(Keys.BACK_SPACE)
    body_element.send_keys(car_body)
    sleep(1) #wait for search to load (wsl)
    body_element.send_keys(Keys.DOWN)
    body_element.send_keys(Keys.RETURN)
    body_element.send_keys(Keys.ESCAPE) 

def get_transmission(driver):
    transmission_element = driver.find_elements(By.XPATH,'//*[@id="sales-by-transmission"]/div[2]/div/div/table/tbody/tr')
    rows = len(driver.find_elements(By.XPATH,'//*[@id="sales-by-transmission"]/div[2]/div/div/table/tbody/tr'))
    cols = len(driver.find_elements(By.XPATH, '//*[@id="sales-by-transmission"]/div[2]/div/div/table/tbody/tr[1]/td'))
    print(rows) 
    print(cols)

    transmission = [None] * rows

    if rows != 0:
        for r in range(1, rows+1): 
            # obtaining the text from each column of the table 
            transmission[r-1] = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[2]/div[9]/div/div[2]/div/div/table/tbody/tr['+str(r)+']/td['+str(2)+']').text
            transmission[r-1] = transmission[r-1].lower()
    
    return transmission

def enter_transmission(driver,car_transmission):
    #find & select make
    transmission_element = driver.find_element(By.XPATH,'//*[@id="app"]/div[4]/div[2]/div/div[1]/div[3]/div[2]/div[4]/div/div[2]/input')
    transmission_element.send_keys(Keys.BACK_SPACE)
    transmission_element.send_keys(car_transmission)
    sleep(1) #wait for search to load (wsl)
    transmission_element.send_keys(Keys.DOWN)
    transmission_element.send_keys(Keys.RETURN)
    transmission_element.send_keys(Keys.ESCAPE) 

def get_county(driver):
    county_element = driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[11]/div/div[2]/div/div/table/tbody/tr')
    rows = len(driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[11]/div/div[2]/div/div/table/tbody/tr'))
    cols = len(driver.find_elements(By.XPATH, '/html/body/div/div[3]/div/div[2]/div[11]/div/div[2]/div/div/table/tbody/tr[1]/td'))
    print(rows) 
    print(cols)

    county = [None] * rows

    if rows != 0:
        for r in range(1, rows+1): 
            # obtaining the text from each column of the table 
            county[r-1] = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[2]/div[11]/div/div[2]/div/div/table/tbody/tr['+str(r)+']/td['+str(2)+']').text

    return county

def get_quant(driver):
    qcounty_element = driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[11]/div/div[2]/div/div/table/tbody/tr')
    rows = len(driver.find_elements(By.XPATH,'/html/body/div/div[3]/div/div[2]/div[11]/div/div[2]/div/div/table/tbody/tr'))
    cols = len(driver.find_elements(By.XPATH, '/html/body/div/div[3]/div/div[2]/div[11]/div/div[2]/div/div/table/tbody/tr[1]/td'))
    print(rows) 
    print(cols)

    qcounty = [None] * rows

    if rows != 0:
        for r in range(1, rows+1): 
            # obtaining the text from each column of the table 
            qcounty[r-1] = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[2]/div[11]/div/div[2]/div/div/table/tbody/tr['+str(r)+']/td['+str(3)+']').text

    return qcounty




def scrape_site (url, driver, thedict, YR, MTH, car_make, engine):
    #List = []
    drop_down_menu(url, driver)
    enter_yr_mth(driver,YR,MTH)
    enter_make(driver, car_make)
    enter_engine(driver,engine)
    click_filter_button(driver)

    car_models=get_models(driver)

    if car_models != [] :
        for n in car_models:
            drop_down_menu(url, driver)
            enter_make(driver, car_make)
            enter_engine(driver,engine)
            enter_model(driver,n)
            click_filter_button(driver)
            
            car_bodies = get_body(driver)

            if len(car_bodies) > 1:
                for i in car_bodies:
                    drop_down_menu(url, driver)
                    enter_body(driver,i)
                    click_filter_button(driver)

                    transmission = get_transmission(driver)
                    if len(transmission) > 1:
                        for x in transmission:
                            drop_down_menu(url, driver)
                            enter_transmission(driver,x)
                            click_filter_button(driver)
                    elif len(transmission) == 1:
                        car_seg = get_seg(driver)
                        car_county = get_county(driver)
                        quant = get_quant(driver)
                        for z in range(0, len(car_county)):
                            List = [YR, MTH, car_make, engine, n, car_seg[0],i,
                                    transmission[0], car_county[z], quant[z]]
                            thedict["Year"].append(List[0])
                            thedict["Month"].append(List[1])
                            thedict["Make"].append(List[2])
                            thedict["Engine"].append(List[3])
                            thedict["Model"].append(List[4])
                            thedict["Segment"].append(List[5])
                            thedict["Body"].append(List[6])
                            thedict["Transmission"].append(List[7])
                            thedict["County"].append(List[8])
                            thedict["Quantity"].append(List[9])
                            

            elif len(car_bodies) == 1:  
                transmission = get_transmission(driver)
                car_seg = get_seg(driver)
                car_county = get_county(driver)
                quant = get_quant(driver)
                for z in range(0, len(car_county)):
                    List = [YR, MTH, car_make, engine, n, car_seg[0], car_bodies[0],
                        transmission[0], car_county[z], quant[z]]
                    thedict["Year"].append(List[0])
                    thedict["Month"].append(List[1])
                    thedict["Make"].append(List[2])
                    thedict["Engine"].append(List[3])
                    thedict["Model"].append(List[4])
                    thedict["Segment"].append(List[5])
                    thedict["Body"].append(List[6])
                    thedict["Transmission"].append(List[7])
                    thedict["County"].append(List[8])
                    thedict["Quantity"].append(List[9])

            print(thedict)

    if thedict["Year"] != []:
        filename = "EVDATA.csv"
        field_names = ["Year", "Month", "Make", "Model",
                    "Segment", "Body", "Engine", "Transmission",
                    "County", "Quantity"]
        # write to  csv file
        with open (filename, 'w') as csvfile:
            #writer = csv.DictWriter(csvfile, fieldnames=field_names)
            
            writer = csv.writer(csvfile)
            key_list = list(thedict.keys())
            limit = len(thedict['Year'])
            #writer.writerows(thedict.keys())
            writer.writeheader()
            for z in range(len(thedict['Year'])):
                writer.writerow([thedict[x][z] for x in key_list])

    # initializing the titles and rows list
    #fields = []
   # rows = []
    
    # List that we want to add as a new row
    #List = [6, 'William', 5532, 1, 'UAE']
    
    # Open our existing CSV file in append mode
    # Create a file object for this file
    # if List != []:
    #     with open(filename, 'a') as f_object:
        
    #         # Pass this file object to csv.writer()
    #         # and get a writer object
    #         writer_object = writer(f_object)
        
    #         # Pass the list as an argument into
    #         # the writerow()
    #         writer_object.writerow(List)
        
    #         # Close the file object
    #         f_object.close()

    # # Open the CSV file for reading
    # with open(filename, mode='r') as file:
    #     # Create a CSV reader with DictReader
    #     csv_reader = csv.DictReader(file)

    #     # Initialize an empty list to store the dictionaries
    #     data_list = []
    #     # Iterate through each row in the CSV file
    #     for row in csv_reader:
    #         # Append each row (as a dictionary) to the list
    #         data_list.append(row)

    # # Print the list of dictionaries
    # for data in data_list:
    #     print(data)
    

   
    # # printing the field names
    # print('Field names are:' + ', '.join(field for field in fields))

    # # printing first 5 rows
    # print('\nFirst 5 rows are:\n')
    # for row in rows[:5]:
    #     # parsing each column of a row
    #     for col in row:
    #         print("%10s" % col, end=" "),
    #     print('\n')





if __name__ == "__main__":
    url = "https://stats.beepbeep.ie/"
    driver = driver_setup()
    count = 0

    YR = (2024,2023)
    #YR = (2024,2023,2022)

    MTH = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]

    #MTHnum = arr.array('i',[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    ENGINE = ["electric", "diesel electric (hybrid)", "diesel/plug-in electric hybrid",
            "petrol electric (hybrid)", "petrol/plug-in electric hybrid"]

    car_make = ["ALFA ROMEO", "AUDI", "BENTLEY", "BMW", "BYD", "CITROEN", "CUPRA",
                "DACIA", "DS", "FERRARI", "FIAT", "FORD", "GWM", "HONDA", "HYUNDAI",
                "JAGUAR", "JEEP", "KIA", "LAND ROVE", "LEXUS", "LOTUS", "MAXUS",
                "MAZDA", "MERCEDES-BENZ", "MG", "MINI", "NISSAN", "OPEL", "PEUGEOT",
                "POLESTAR", "PORSCHE", "RENAULT", "SEAT", "SKODA", "SMART",
                "SSANGYONG", "SUBARU", "SUZUKI", "TESLA", "TOYOTA", "VOLKSWAGEN",
                "VOLVO"]
    
    thedict = {"Year": [], "Month":[], "Make":[], "Model":[],
            "Segment":[], "Body":[], "Engine":[], "Transmission":[],
            "County":[], "Quantity":[]}
    #df = pd.read_csv('EVDATA.csv') 
   
    for i in YR:
        for n in MTH:
            for z in car_make:
                for x in ENGINE:
                    scrape_site(url, driver, thedict, i, n, z, x)
                    count = count+1
                    sleep (2)

