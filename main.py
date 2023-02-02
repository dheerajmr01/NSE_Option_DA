from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


website = "https://www.nseindia.com/option-chain"
path = "C:/Users/dheer/OneDrive/Desktop/Options/chromedriver.exe"
chromeOptions = webdriver.ChromeOptions()
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, chrome_options=chromeOptions)


driver.get(website)
sleep(3)
driver.find_element(by="xpath", value='//div[@class="xlsdownload"]').click()
sleep(7)
