from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import platform
import ExcelFunctions
import openpyxl
import time

#driver = webdriver.Edge(executable_path="C:\Drivers\msedgedriver.exe")
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
#driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe")
#driver = webdriver.Opera(executable_path="C:\Drivers\operadriver.exe")

path = "C://Users//Mikhail//PycharmProjects//spbrealty.ru//CheckList.xlsx"

#write result at next column
book = openpyxl.load_workbook(path)
sheet = book.active
num = sheet.max_column + 1

#Header of checklist
ExcelFunctions.writeData(path, "List1", 1, num, platform.platform())
ExcelFunctions.writeData(path, "List1", 2, num, driver.capabilities['browserName'])
ExcelFunctions.writeData(path, "List1", 3, num, driver.capabilities['browserVersion'])
#ExcelFunctions.writeData(path, "List1", 3, num, driver.capabilities['version']) #case opera
ExcelFunctions.writeData(path, "List1", 4, num, datetime.now().strftime('%d.%m.%Y_%H.%M.%S'))

#Opens main page
driver.maximize_window()
driver.get("https://www.spbrealty.ru/")
driver.implicitly_wait(30)
window_before = driver.window_handles[0]
ExcelFunctions.writeData(path, "List1", 6, num, "Pass")
time.sleep(13)
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.save_screenshot("C://Users//Mikhail//PycharmProjects//spbrealty.ru//screenshots//homepage.png")

#Check title
title = "Петербургская Недвижимость 🏠 - купить квартиру, жилая, элитная, загородная и коммерческая недвижимость Санкт-Петербурга"
assert title in driver.title, "title is wrong"
ExcelFunctions.writeData(path, "List1", 7, num, "Pass")

#Logo is visible
logo = driver.find_element_by_id("emerge-header")
if logo.is_displayed():
    ExcelFunctions.writeData(path, "List1", 8, num, "Pass")
else:
    ExcelFunctions.writeData(path, "List1", 8, num, "Fail")


#Left click on lk button
try:
    driver.find_element_by_xpath('//*[@id="emerge-header"]/div[2]/div/div[1]/a/span').click()
except WebDriverException:
    ExcelFunctions.writeData(path, "List1", 9, num, "Fail")
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.implicitly_wait(30)
ExcelFunctions.writeData(path, "List1", 9, num, "Pass")

#Enter login
driver.find_element_by_name("phone").send_keys("9523813251")
ExcelFunctions.writeData(path, "List1", 10, num, "Pass")

#Enter password
driver.find_element_by_name("password").send_keys("94!h87!D") #vy nichego ne videli
ExcelFunctions.writeData(path, "List1", 11, num, "Pass")

#Click login button
driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div/div[1]/form/div[3]/div[1]/button').click()
ExcelFunctions.writeData(path, "List1", 12, num, "Pass")

#close the browser
driver.quit()