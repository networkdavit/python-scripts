#pip3 install selenium webdriver-manager

import json
import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

firefox_options = Options()
firefox_options.add_argument("--headless")  
firefox_options.set_preference("network.proxy.type", 0)  # Disables proxy, if you don't use any proxies, feel free to remove this line

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

url = sys.argv[1] 
driver.get(url)

driver.implicitly_wait(5)

cookies = driver.get_cookies()

local_storage = driver.execute_script("return window.localStorage;")

with open('cookies.json', 'w') as cookie_file:
    json.dump(cookies, cookie_file, indent=4)

with open('local_storage.json', 'w') as local_storage_file:
    json.dump(local_storage, local_storage_file, indent=4)


driver.quit()

print("Cookies and local storage saved successfully.")
