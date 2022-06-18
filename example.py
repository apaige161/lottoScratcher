
# scrape "https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html"

from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
import time

# setup
options = webdriver.ChromeOptions()
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

weatherWebsite = "https://weather.com/"
lotteryWebsite = "https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html"
kyFishAndWildlife = "https://fw.ky.gov/Pages/default.aspx"

# open website
driver.get(kyFishAndWildlife)
# wait for item to be clickable, timeout after 10 seconds
maxTimeout = 10
wait = WebDriverWait(driver, maxTimeout, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
search = wait.until(EC.element_to_be_clickable((By.ID, "enterprise-search-text")))
print("Home page loaded")

# time.sleep(5)

# get title
title = driver.title
print(title)

# enter something into search bar
search.clear()
search.send_keys("bear")
# press enter
search.send_keys(Keys.RETURN)

# wait for elements to show up
elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "footer-title")))
print("Search page loaded")

# capture article titles
articleNames = driver.find_elements(By.XPATH, '//*[@id="results"]/ul/li/a')

print("article titles only")
for article in articleNames:
    print(article.text)

print("printing footer elements")
for element in elements:
    print(element.text)

# click on first search element
classLink = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Education Classes")))
print(classLink.text)
classLink.click()

# wait for elements to show up
boatLink = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Boat-Ed.com Course")))
print("Education classes page loaded, found " + str(boatLink.text) )
boatLink.click()

# buyLicense = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Buy License")))
# print("Buy License page loaded, found " + str(buyLicense.text) )
# buyLicense.click()

# buyLicensebutton = wait.until(EC.presence_of_element_located((By.ID, "ButtonCurrent")))
# print("Buy License page loaded, found " + str(buyLicensebutton.text) )
# buyLicensebutton.click()



# close browser
driver.quit() 



