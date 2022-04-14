
# scrape "https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html"

from pydoc import classname
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
import time

# setup
options = webdriver.ChromeOptions()
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

KYlotteryWebsite = "https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html"

# Open website and sort by price
driver.get(KYlotteryWebsite)
# Wait for item to be clickable
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
# Select "Price" in the dropdown to sort items 
dropDownPriceOption = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/select/option[4]')))
print("Page Loaded Successfully")
dropDownPriceOption.click()
goButton = driver.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div')
goButton.click()

# Collect 2D array of lotto tickets for each price point

# Get each price point
pricesArray = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "klc-scratch-price_section")))
for prices in pricesArray:
    print(prices.text)

# Get all tickets
tickets = driver.find_elements(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[2]/ul/li/a')
for ticket in tickets:
    print(ticket.text)

    # Click on each ticket
    ticket = driver.find_element(By.LINK_TEXT, ticket.text)

    # Wait for page to load 
    table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'panel-body')))

    # Get name
    ticketName = driver.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/h2')
    print(ticketName.text)

    # Get Value
    value = driver.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/div/div[1]/div[2]/div[1]/b[4]')

    # Get Top Prize

    # Get Overall Odds
    odds = driver.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/div/div[1]/div[2]/div[1]/b[6]')

    # Get Game #
    gameNum = driver.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/div/div[1]/div[2]/div[1]/b[7]')

    # Remove "- number" 
    splitTicket = ticketName.text.split(" ", 1)
    pureTicketName = splitTicket[0]


    print("Name: " + pureTicketName)
    print("Value: " + value)
    print("Ticket Number: " + gameNum)
    print("Odds: " + odds)



    # Get table data
    input()




# close browser
#driver.quit() 