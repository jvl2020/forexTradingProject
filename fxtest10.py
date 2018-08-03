import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import csv
import urllib
from collections import defaultdict

url = 'https://www.tradingview.com/forex-screener/'
driver = webdriver.Chrome(executable_path=r"C:\Users\Jay Dave\Downloads\chromedriver\chromedriver.exe")
driver.get(url)

def get_elements_by_xpath(driver, xpath):
    return [entry.text for entry in driver.find_elements_by_xpath(xpath)]
    

data = driver.find_element_by_xpath('//*[@id="js-screener-container"]/div[4]/table/tbody').text


search_entries = [("tickers", "//tbody/tr/td[1]/div/a"),("bid","//tbody/tr/td[7]"), ("ask","//tbody/tr/td[8]"), ("rating","//tbody/tr/td[11]")]


entries = []

x = 1
while True:
    print(data)
    time.sleep(30)
    
driver.quit()

