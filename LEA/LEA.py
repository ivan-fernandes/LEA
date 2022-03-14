import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException

from email_LEA import send_email

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
url = "https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/5d4ffe1a-fabf-4231-8599-55cf699a382f?dswid=4946&dsrid=640&st=2&v=1647255436709"


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
