#Created 31/01/2025
#Author Úna Cotter
#Scapper for scappoign data from stats.beepbeep.ie

import requests
response = requests.get("https://stats.beepbeep.ie/")
if response.status_code == 200:
    print("Website Accessed Successfully.")
else:
    print("Issue Accessing Website")