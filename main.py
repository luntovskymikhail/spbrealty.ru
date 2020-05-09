from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import platform
import ExcelFunctions
import openpyxl

driver = webdriver.Ie(executable_path="C://Drivers//IEDriverServer.exe")
path = "C://Users//Mikhail//PycharmProjects//spbrealty.ru//CheckList.xlsx"

#write result at next column
book = openpyxl.load_workbook(path)
sheet = book.active
num = sheet.max_column + 1

#Header of checklist
ExcelFunctions.writeData(path, "List1", 1, num, platform.platform())
ExcelFunctions.writeData(path, "List1", 2, num, driver.capabilities['browserName'])
ExcelFunctions.writeData(path, "List1", 3, num, driver.capabilities['browserVersion'])
ExcelFunctions.writeData(path, "List1", 4, num, datetime.now().strftime('%d.%m.%Y_%H.%M.%S'))

#Opens main page
driver.maximize_window()
driver.get("https://www.spbrealty.ru/")
ExcelFunctions.writeData(path, "List1", 6, num, "Pass")
#time.sleep(13)


#Left click on lk button
#driver.find_element_by_xpath('//*[@id="emerge-header"]/div[2]/div/div[1]/a/span').click()

#Declares end time of test run and closing the browser
driver.quit()