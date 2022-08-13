

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# options = Options()
# options.add_argument("user-data-dir=/tmp/tarun")
driver = webdriver.Chrome("/usr/bin/chromedriver")
chrome_options = Options()
chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://cvdsfefvd.click/V1L2dhbWVzL2NyYXNoL2luZGV4")

time.sleep(60)
cookies = driver.get_cookies()
for cookie in cookies:
    with open('cookies.txt', 'a') as stored_cookies:
        stored_cookies.write(str(cookie) + '\n')

driver.quit()