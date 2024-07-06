# important notice for linux users, do the steps below to get this to work
# pip install selenium or pip3 install selenium
# wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
# tar -xvzf geckodriver-v0.34.0-linux64.tar.gz
# sudo mv geckodriver /usr/local/bin/
# geckodriver --version


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

def google_search(query):
    options = Options()
    options.headless = False  # Change to True for headless mode 

    gecko_path = '/usr/local/bin/geckodriver'  # put path for geckodriver
    service = Service(executable_path=gecko_path)

    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(3)

        print("Page title is:", driver.title)
        

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

search_query = "Cyberyozh"
google_search(search_query)
