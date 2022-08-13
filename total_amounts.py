from datetime import datetime
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb://admin:password@localhost:27017/?authMechanism=DEFAULT")

from calendar import day_abbr
import time
from traceback import print_tb
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options 
from bson import ObjectId
driver = webdriver.Chrome("/usr/bin/chromedriver")
chrome_options = Options()
chrome_options.add_argument("----start-maximized")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://cvdsfefvd.click/")
with open('cookies.txt') as stored_cookies:
    while True:
        line = stored_cookies.readline()
        if line == '':
            print('End Of File')
            break 
        cookie = eval(line)
        driver.add_cookie(cookie)
driver.get("https://cvdsfefvd.click/V1L2dhbWVzL2NyYXNoL2luZGV4")

time.sleep(10)
try:
    ads = driver.find_element("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "splash-close-button", " " ))]').click()
except:
    pass
try:
    start_buttom = driver.find_element("xpath",'//*[(@id = "play_button")]').click()
except :
    print("log in need")
time.sleep(4)
history = driver.find_element("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "tab-div-2", " " ))]').click()
time.sleep(1)
max_p = 0 
max_l = 0
total_profit = 0
total_loss = 0
first_time = True
tt = 0
counter = 0

positive_counter = 0
nagative_counter = 0
while True:
    profit = 0
    loss = 0
    total_money_per = 0
    table_body = driver.find_elements("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "h-col-1", " " ))]')
    if "-" not in table_body[1].text:
        data_users = driver.find_element("xpath",'//*[(@id = "desktop-users")]')
        data_users = data_users.text.splitlines()
        for item_index in range(3,len(data_users),4):
            if data_users[item_index] == "-":
                loss+=int(data_users[item_index-1].replace(",",""))
            else:
                profit+= int(data_users[item_index].replace(",",""))
            total_money_per += int(data_users[item_index-1].replace(",",""))
        total_profit+=profit
        total_loss+=loss
        time.sleep(5)
        last_tt = tt
        tt = total_loss  - total_profit
        if first_time is True:
            max_l = tt 
            max_p = tt
            client.BetDB.maximums.find_one_and_update({"_id":ObjectId("62f79e9aa035f8061215ca91")},{"$set":{"max_loss":tt}})
            client.BetDB.maximums.find_one_and_update({"_id":ObjectId("62f79e9aa035f8061215ca91")},{"$set":{"max_profit":tt}})
            first_time = False

        else:
            if tt < max_l :
                max_l = tt
                client.BetDB.maximums.find_one_and_update({"_id":ObjectId("62f79e9aa035f8061215ca91")},{"$set":{"max_loss":tt}})
            elif tt > max_p:
                max_p = tt
                client.BetDB.maximums.find_one_and_update({"_id":ObjectId("62f79e9aa035f8061215ca91")},{"$set":{"max_profit":tt}})
        if float(table_body[1].text) > 1.8:
            positive_counter+=1
        else:
            nagative_counter+=1
        client.BetDB.rounds.insert_one({"counter":counter,"cash":tt ,"last_cash":last_tt,"mul_game":float(table_body[1].text),"total_money_per":total_money_per,"maxium_cash_profit":max_p,"maxium_cash_loss":max_l,"delta":positive_counter - nagative_counter,"submit_date":datetime.utcnow()})
        
        time.sleep(3)
# time.sleep(5)
# history = driver.find_element("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "tab-div-2", " " ))]').click()
# time.sleep(4)

