from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
import os



website = "https://www.nseindia.com/option-chain"
path = "C:/Users/dheer/OneDrive/Desktop/Options/chromedriver.exe"
chromeOptions = webdriver.ChromeOptions()

p = {"download.default_directory" : "D:\\Projects\\NSE_Option_DA"}
chromeOptions.add_experimental_option("prefs",p)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=chromeOptions)

driver.get(website)
sleep(3)
driver.find_element(by="xpath", value='//div[@class="xlsdownload"]').click()
sleep(7)
driver.close()


