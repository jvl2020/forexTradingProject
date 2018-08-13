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
import datetime

url = 'https://www.tradingview.com/forex-screener/'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r"C:\Users\Jay Dave\Downloads\chromedriver\chromedriver.exe", chrome_options=options)
driver.get(url)



with open(r'C:\Users\Jay Dave\Documents\fxdatatest.csv', 'a', newline= '') as f_output:   
    csv_output = csv.writer(f_output)
    while True:
        try:
            driver.refresh()
            time.sleep(3)
            data = driver.find_element_by_xpath('//*[@id="js-screener-container"]/div[4]/table/tbody').text.split('\n')
            for elem in data:
                if "Strong" not in elem:
                    parts = elem.split(' ')
                    fxn = parts[0]
                    fxp = parts[-8]
                    fxs = parts[-1]
                    fxb = parts[-5]
                    fxa = parts[-4]
                    print(fxn)
                    csv_output.writerow([fxn + " " + fxp + " " + fxs + " " + fxb + " " + fxa])
                elif "Strong" in elem:
                    parts = elem.split(' ')
                    fxn = parts[0]
                    fxp = parts[-9]
                    fxs = parts[-2] + parts[-1]
                    fxb = parts[-6]
                    fxa = parts[-5]
                    print(fxn)
                    csv_output.writerow([fxn + " " + fxp + " " + fxs + " " + fxb + " " + fxa])
            csv_output.writerow([datetime.datetime.now().strftime("%Y-%m-%d")])
            f_output.flush()
        except NoSuchElementException:
            pass
        time.sleep(897)

driver.quit()

