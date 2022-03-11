import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
sth = True

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
webdriver_service = Service("chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
wait = WebDriverWait(browser,5)

browser.get("https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng?sprachauswahl=en")

print(browser.current_url)

# name_box = wait.until(
#     EC.presence_of_all_elements_located(
#         (By.XPATH, '//*[@id="xi-cb-1"]')))
# name_box.click()


# button_next = wait.until(
#     EC.presence_of_all_elements_located(
#         (By.XPATH, '//*[@value="Next"]')))
# button_next.click()

# WebDriverWait(browser,10)
time.sleep(5)
ID = browser.find_element(By.XPATH, '//*[@id="xi-cb-1"]')
ID.click()

time.sleep(1)
next = browser.find_element(By.XPATH, '//*[@id="applicationForm:managedForm:proceed"]')
next.click()

# time.sleep(5)
# description = browser.find_element(By.NAME, "description").get_attribute("content")
# print(f"{description}")

time.sleep(10)
print(browser.current_url)
citizenship = browser.find_element(By.XPATH, '//*[@id="xi-sel-400"]/option[31]')
citizenship.click()

time.sleep(1)
applicants = browser.find_element(By.XPATH, '//*[@id="xi-sel-422_1"]')
applicants.click()

time.sleep(1)
live_alone = browser.find_element(By.XPATH, '//*[@id="xi-sel-427_2"]')
live_alone.click()

time.sleep(10)
applyfor = browser.find_element(By.XPATH, '//*[@id="SERVICEWAHL_EN3327-0-1"]')
applyfor.click()

time.sleep(5)
educational = browser.find_element(By.XPATH, '//*[@id="SERVICEWAHL_EN_327-0-1-3"]')
educational.click()

time.sleep(5)
study = browser.find_element(By.XPATH, '//*[@id="SERVICEWAHL_EN327-0-1-3-305244"]')
study.click()

time.sleep(5)
next2 = browser.find_element(By.XPATH, '//*[@id="applicationForm:managedForm:proceed"]')
next2.click()

time.sleep(5)
description = browser.find_element(By.NAME, "description").get_attribute("content")
print(f"{description}")

#Wait for 10 seconds
time.sleep(10)
browser.quit()





### RUN IT AUTOMATICALLY AT A SPECIFIC TIME INTERVAL

# while sth == True:
#     # browser = webdriver.Chrome(ChromeDriverManager().install())
#     browser = webdriver.Chrome(ChromeDriverManager().install())
#     browser.get("https://www.calvintorra.com/blog/how-i-saved-8-hours-automating-my-gov-appointment-hunt-using-python")


# # fake scrolling down and find specific fields
#     niebox = WebDriverWait(browser, 10).until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, '//*["id="applicationForm:managedForm:proceed"]')))

#     niebox.click()
#     # niebox.send_keys("E487XXXXX")

#     name_box = WebDriverWait(browser,10).until(
#         EC.presence_of_all_elements_located(
#             (By.XPATH, '//input[@id="xxTXTxx"]')))

#     time.sleep(2)
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     name_box.click() # click on a button
#     name_box.send_keys("Calvin T") # input text to a field


#     # check if there are appointments or not
#     no_appointments = browser.page_source.find("There are currently no dates available for the selected service! Please try again later.")

#     if no_appointments:
#         browser.close()
#         time.sleep(600)
#     else:
#         os.system("YAY!! Appointments are available!")
#         ### check the code to sound a buzz for X seconds
#         time.sleep(2)
#         os.system("YAY!! Appointments are available!")
#         ### code to sound a buzz again
#         time.sleep(2)
#         lets_go = False
#     break # break from while loop
