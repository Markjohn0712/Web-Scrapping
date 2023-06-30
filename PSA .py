# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:40:16 2023

@author: Mark Joseph Pulido
"""

#dependencies

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#verification_code_elements = soup.select ()

# Set up Chrome driver with custom download directory
chrome_options = Options()
chrome_options.add_argument("--disable-GPU")
chrome_options.add_argument("--kiosk-printing") # Open print dialog automatically

settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], "selectedDestinationId": "Save as PDF", "version": 2}
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings), 'savefile.default_directory':r"C:\Users\pulid\OneDrive\Desktop\Mark Joseph Python",  "download.name":"gaga     6667"}
            
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(r"D:\Evan Files\OneDrive - Polytechnic University of the Philippines\School Docs\3rd Year DCET\2nd  Sem\HYT FILES\Tech Core Unit\Tasks\Web Scraping bot Crawling\Code\My Codes\chromedriver.exe", options=chrome_options)

# Access the URL
driver.get("https://psa.gov.ph/user")

last_name = input("Please enter your last name: ")
first_name = input("PLease enter your first name: ")

# Find the last name input element and send the user input
last_name_input = driver.find_element(By.ID, "inputLastName")
last_name_input.send_keys(last_name)

# Find the first name input element and send the user input
first_name_input = driver.find_element(By.ID, "inputFirstName")
first_name_input.send_keys(first_name)

# Locate and click the search button
search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
search_button.click()

# Wait for the search results to load
time.sleep(5)

driver.execute_script('window.print();')

# Simulate pressing Ctrl+P to open the print dialog
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'p')

# Click the "Print" button
#print_button = driver.find_element(By.ID, "ctl00_cpExclusions_Button1")
#print_button.click()

# Wait for the download to complete (you may need to adjust the wait time based on the file size and network speed)
time.sleep(3)

#__________________________________________

# Simulate pressing Ctrl+P to open the print dialog
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'p')

# Close the WebDriver
driver.quit()