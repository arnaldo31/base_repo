from seleniumbase import Driver
from bs4 import BeautifulSoup

driver = Driver(uc=True,headless=True)
driver.get('https://seleniumbase.io')
page = BeautifulSoup(driver.page_source,'html.parser')
print(page.h1.text)
