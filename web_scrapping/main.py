from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

url = 'https://microdata.unhcr.org/index.php/catalog/292/data-dictionary/F1?file_name=UNHCR_JOR_2020_HV9v2_data_household_v2'

# s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)
print("")

# container-fluid variables-container
# var-id text-break
# //*[@id="b354cab57768c7d4c1106eb4e82c75dc"]

# //*[@id="variables-container"]/div[1]

columns = driver.find_elements(By.CLASS_NAME, 'container-fluid table-variable-list data-dictionary')
print(columns)
for column in columns:
    name = column.find_elements(By.XPATH, './/*[@id="variables-container"]/div[1]')
    print(name)

