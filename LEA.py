from multiprocessing.sharedctypes import Value
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException

from email_LEA import send_email
import ipdb


## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")

# Set path to chromedriver as per your configuration
webdriver_service = Service("/usr/bin/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
wait = WebDriverWait(browser,5)
wait2 = WebDriverWait(browser,30)
url = "https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/3f5e70cf-3b3b-42e9-bef3-68324b320a4b?dswid=8583&dsrid=609&v=1646210778433&st=2"

# browser.get("https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/2e64240f-d1ab-48fc-8b7e-0cfaacb531d3?dswid=3231&dsrid=815&st=2&v=1646159904202")
# browser.get("https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/3f5e70cf-3b3b-42e9-bef3-68324b320a4b?dswid=1051&dsrid=824&st=2&v=1646207503266")


##### get the current time
### pop a window up
### sound a buzz


r'''
XPATH_calendar = '//*[@id="xi-div-2"]/div'   # calendar
XPATH_calendarTable = '//*[@id="xi-div-2"]/div/div[1]/table'   # calendar table
legend = '//*[@id="xi-fs-2"]/legend' # this should be Auswahl Termin, as a text()
appointment_date = '//*[@id="xi-div-2"]/div/div[1]/table/tbody/tr[3]/td[2]/a' # text or value would be a number from 1 to 30

data-handler = selectDay
data-event = click
data-year = 2022
'''


while True:
    browser.get(url)
#    ipdb.set_trace()
    print(browser.current_url)
    a = 1
#     browser.execute_script("return arguments[0].scrollIntoView(true);", wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="applicationForm:managedForm:proceed"]'))))
#     browser.find_element(By.XPATH, '//*[@id="applicationForm:managedForm:proceed"]').click()
#     print("Navigating to Next Page")
#     url2 = browser.current_url
#     print(f"Next page: {url2}")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="messagesBox"]'))))
#     print("found message box")


    try:
        print("--")
        browser.execute_script("return arguments[0].scrollIntoView(true);", wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="applicationForm:managedForm:proceed"]'))))
        browser.find_element(By.XPATH, '//*[@id="applicationForm:managedForm:proceed"]').click()
        print("Pressing next")
        browser.execute_script("return arguments[0].scrollIntoView(true);", wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="xi-sel-427"]'))))
        # browser.find_element(By.XPATH, '//*[@id="messagesBox"]/ul/li')
        print("Found list box. No appointments available!")
        # browser.close()
        time.sleep(300)
        print("----------------------------------")
        print(f"Trial number: {a}")
        a+=1
        url = browser.current_url
    except:
        print("Appointment might be available. Go check it out")
        send_email()
        time.sleep(2)
        break # break from while loop



# time.sleep(5)
# description = browser.find_element(By.NAME, "title").get_attribute("content")
# print(f"{description}")

# print(browser.find_element(By.XPATH, '//*[@id="messagesBox"]'))

# time.sleep(2)
# next2 = browser.find_element(By.XPATH, '//*[@id="applicationForm:managedForm:proceed"]')
# next2.click()

# time.sleep(10)
# description = browser.find_element(By.NAME, "title").get_attribute("content")
# print(f"{description}")

# time.sleep(1)
# # no_appointments = browser.find_element(By.XPATH, '//*[@id="messagesBox"]/ul/li')
# # no_appointments = browser.find_element(By.XPATH, '//*[contains(text(), "There are currently no dates available for the selected service!")]')
# # no_appointments = browser.find_element(By.XPATH, '//*[text()="There are currently no dates available for the selected service!"]')
# # print(no_appointments)

# # errorMSG = browser.find_element(By.XPATH, '//*[@id="messagesBox"]/ul/li/text()')
# # print(errorMSG)

# #Wait for 10 seconds
# # time.sleep(10)
# browser.quit()
