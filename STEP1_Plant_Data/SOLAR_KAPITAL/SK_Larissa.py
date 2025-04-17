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
from selenium.webdriver.support.ui import WebDriverWait
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
name_folder="DATA_SK_Larissa"
path_out=os.path.join(head_tail[0], name_folder)
print(path_out)
shutil.rmtree(path_out, ignore_errors=True)
isExist = os.path.exists(path_out) 
if not isExist: 
   os.makedirs(path_out)
print("DATA for Larissa  from Solar Kapital are beeing send here: ")
print(path_out)

# Set up the Chrome driver
#driver = webdriver.Chrome()
chrome_options = Options()
prefs = {'profile.default_content_setting_values.automatic_downloads': 1, 'download.default_directory': path_out }
#prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the data loger: (NOT GOOD)
driver.get('https://www.auroravision.net/dashboard/#27923567')

# --- Interact with the webpage via html 
# ---- Log in 
username_field = driver.find_element(By.ID, "userId")
password_field = driver.find_element(By.ID,"password") 
username_field.send_keys('<userID>')
password_field.send_keys('<password>')
password_field.send_keys(Keys.RETURN)

# DAILY DATA

# Go to MTD tab

#time.sleep(7)
wait = WebDriverWait(driver, 10)
xpath= '/html/body/div[1]/av-frame/main/av-dashboard/div/div/div/div/div/av-plant-performance/div/av-plant-performance-chart/av-daterange-with-interval/av-duration-selector/div/ul/li[6]'
element= wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
#button_day = driver.find_element('xpath', '/html/body/div[1]/av-frame/main/av-dashboard/div/div/div/div/div/av-plant-performance/div/av-plant-performance-chart/av-daterange-with-interval/av-duration-selector/div/ul/li[6]')
#button_day= driver.find_element( 'xpath', "//button[@class='cux-tab ui-tab active']")

#button_day= driver.find_element( 'xpath', '//a[contains(@class, "cux-tab ui-tab active"]')
element.click()
exit()

button_day.click()

exit()
time.sleep(5)

#--- Set the month range for data download
#first_month = datetime.strptime('202212', "%Y%m") 
#last_month = datetime.strptime('202301', "%Y%m") 

first_month = '202211'
last_month = '202302'

for i in range(int(first_month), int(last_month)+1):
    year=str(i)[0:4]
    month=str(i)[4:7]
    if int(month) >= 1 and int(month) <= 12:
        start_date= datetime.strptime(f'{year}-{month}-01', "%Y-%m-%d") 
        end_date=start_date.replace(day=1) + relativedelta(months=1) - relativedelta(days=1)
        start_date_key = str(start_date)[0:10]
        end_date_key = str(end_date)[0:10]
        print(f'Download Data for: {start_date_key} to {end_date_key}')
        try:
             button_start_date = driver.find_element('xpath', '/html/body/div[1]/av-frame/main/av-dashboard/div/div/div/div/div/av-plant-performance/div/av-plant-performance-chart/av-daterange-with-interval/div/av-daterange/div/av-datepicker[1]/div/input')
             button_start_date.clear()
             button_start_date.send_keys(start_date_key)
             button_start_date.send_keys(Keys.RETURN)
        except NoSuchElementException:
             print("Element not found, moving to the next step")
        try:
             button_end_date = driver.find_element('xpath', '/html/body/div[1]/av-frame/main/av-dashboard/div/div/div/div/div/av-plant-performance/div/av-plant-performance-chart/av-daterange-with-interval/div/av-daterange/div/av-datepicker[2]/div/input')
             button_end_date.clear()
             button_end_date.send_keys(end_date_key)
             button_end_date.send_keys(Keys.RETURN)
             time.sleep(3)  
        except NoSuchElementException:
           print("Element not found, moving to the next step")
        try:
           element=driver.find_element('xpath', '/html/body/div[1]/av-frame/main/av-dashboard/div/div/div/div/div/av-plant-performance/div/av-plant-performance-chart/div[1]/button/span') 
           driver.execute_script("arguments[0].click();", element)
        except NoSuchElementException:
           print("Element not found, moving to the next step")

        time.sleep(3)




