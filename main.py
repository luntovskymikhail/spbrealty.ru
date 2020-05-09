from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import platform
import ExcelFunctions

driver = webdriver.Opera(executable_path="C:\Drivers\operadriver.exe")
path = "C://Users//Mikhail//PycharmProjects//spbrealty.ru//CheckList.xlsx"
driver.maximize_window()

#Opens main page
driver.get("https://www.spbrealty.ru/")
ExcelFunctions.writeData(path, "List1", 5, 2, "Pass")
time.sleep(13)


#Left click on lk button
#driver.find_element_by_xpath('//*[@id="emerge-header"]/div[2]/div/div[1]/a/span').click()

#Declares end time of test run and closing the browser
driver.quit()


'''
title = "Петербургская Недвижимость 🏠 - купить квартиру, жилая, элитная, загородная и коммерческая недвижимость Санкт-Петербурга"

#Creating log file + puts system info and start time inside
file = '%s_%s' % (datetime.now().strftime('%d.%m.%Y_%H.%M.%S'), 'testrun.txt')

date format datetime.now().strftime('%d.%m.%Y_%H.%M.%S')

open(file, 'w').write("Operation system: " + platform.platform() + "\n")
open(file, 'a').write("Browser name: " + driver.capabilities['browserName'] + "\n")
open(file, 'a').write("Browser version: " + driver.capabilities['version'] + "\n" + "\n")
open(file, 'a').write("Started at: " + datetime.now().strftime('%d.%m.%Y_%H.%M.%S') + "\n" + "\n")

if driver.title == title:
    open(file, 'a').write("Step 1: Pass (Title name is correct)" + "\n")
else:
    open(file, 'a').write("Step 1: Fail (Title name is correct)" + "\n")

open(file, 'a').write("Step 2: Pass (Opens Auth page)" + "\n" + "\n")

open(file, 'a').write("Ended at: " + datetime.now().strftime('%d.%m.%Y_%H.%M.%S'))

'''