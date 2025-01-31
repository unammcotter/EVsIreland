#Created 30/01/2025
#Author Úna Cotter
#Scapper File test area

import requests
response = requests.get("https://stats.beepbeep.ie/")
if response.status_code == 200:
    print("Website Accessed Successfully.")
else:
    print("Issue Accessing Website")