import os
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time

# temp directory checking segment
current_dir = os.getcwd()

temp_dir = f'{current_dir}/temp'

print(f"Checking if {temp_dir} is available...")

if os.path.isdir(f"{temp_dir}"):
    print(f"{temp_dir} is available...")
else:
    print(f"{temp_dir} is not available!!!")
    print(f"Creating new directory {temp_dir}...")
    os.makedirs(f"{temp_dir}")
    print(f"Creating new directory {temp_dir} has been finished...")

URL_API = "https://www.bccondosandhomes.com/public/api2/search-listings"
URL_GET_ACTIVE = "https://www.bccondosandhomes.com/search-listings/"
URL_GET_SOLD = "https://www.bccondosandhomes.com/search-listings/?listing_status=sold"

def get_data():
    # driver = webdriver.Chrome()
    driver = uc.Chrome(use_subprocess=True)
    driver.get(URL_GET_ACTIVE)
    element = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    # element.send_keys(phone)
    time.sleep(10)
    element.send_keys(Keys.RETURN)
    time.sleep(10)
    element = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    # element.send_keys(password)
    element.send_keys(Keys.RETURN)
    time.sleep(15)  # waiting 3 minutes after executed login form submission
    driver.close()  # chrome will be automatically closed after 3 minutes

if __name__ == '_main_':
    get_data()