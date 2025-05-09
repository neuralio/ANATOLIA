from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options
import shutil
import sys 
import os
import shutil 


# Define path to output the downloaded data 
#path_out="/Users/paraskevivourlioti/Documents/NEURALIO/KYKLOS/DATA_KYKLOS/SolarKapital"

print(os.getcwd())
path_here=os.getcwd()
head_tail = os.path.split(path_here)
print(head_tail[0])
name_folder="DATA_SK_Sitia"
path_out=os.path.join(head_tail[0], name_folder)
print(path_out)
#shutil.rmtree(path_out, ignore_errors=True)
isExist = os.path.exists(path_out) 
if not isExist: 
   os.makedirs(path_out)

print("DATA for Sitia from Solar Kapital are beeing send here: ")
print(path_out)

# Set up the Chrome driver
#driver = webdriver.Chrome()
chrome_options = Options()
prefs = {'profile.default_content_setting_values.automatic_downloads': 1, 'download.default_directory': path_out }
#prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the data loger: (NOT GOOD)
driver.get('https://www.sunnyportal.com/Templates/Start.aspx?ReturnUrl=%2f')

# --- Interact with the webpage via html 
# ---- Log in 
username_field = driver.find_element(By.ID, "txtUserName")
password_field = driver.find_element(By.ID,"txtPassword") 
username_field.send_keys('<userID>')
password_field.send_keys('<password>')
password_field.send_keys(Keys.RETURN)

# Navigate to the Specific PLANT
driver.get('https://www.sunnyportal.com/RedirectToPlant/e4b74a68-01f9-45bb-9d36-aff6657d7930')
time.sleep(5)

# Accept Cookies
allow_cookies = driver.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]')
allow_cookies.click()

# DAILY DATA

# Go to MONTH tab
#button_month = driver.find_element('xpath', '/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span/span')
button_month = driver.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_UserControlShowDashboard1_UserControlShowEnergyAndPower1_LinkButton_TabBack1"]')
button_month.click()
time.sleep(5)

#--- Set the month range for data download
first_month = 201205 
last_month = 201712

for i in range(int(first_month), int(last_month)+1):
    year=str(i)[0:4]
    month=str(i)[4:7]
    if int(month) >= 1 and int(month) <= 12:
        print(f'Download Data for: {month}/{year}')
        year_option=int(year)-2009
        try:
           button_year = driver.find_element('xpath', f'/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select[2]/option[{year_option}]')
           button_year.click()
           time.sleep(3)
        except NoSuchElementException:
           print("Element not found, moving to the next step")
        try:
           button_month = driver.find_element('xpath', f'/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr/td[2]/select[1]/option[{month}]')
           button_month.click()
           time.sleep(4)
        except NoSuchElementException:
           print("Element not found, moving to the next step")
        try:
           element=driver.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_UserControlShowDashboard1_UserControlShowEnergyAndPower1_ImageButtonDownload"]') 
           driver.execute_script("arguments[0].click();", element)
           time.sleep(5)
        except NoSuchElementException:
           print("Element not found, moving to the next step")




