
# scrape "https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html"

from fileinput import filename
from pydoc import classname
from re import I
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
import time
from ticketClass import Ticket
from ticketClass import createTicket
from os import path
import csv


start_time = time.time()


# setup
options = webdriver.ChromeOptions()
PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
JSON_file = "./ticketData.json"
KYlotteryWebsite = 'https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html'

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

# Get all ticket names
tickets = driver.find_elements(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[2]/ul/li/a')

ticketNameArr = []

for ticket in tickets:
    #add ticket text only to new array
    ticketNameArr.append(ticket.text)
print("Number of tickets found: " + str(len(tickets)))

print("inside ticket name array")
for ticket in ticketNameArr:
    print("Ticket Name: " + ticket)
print("end ticket name array")
print("start loop iteration")


allTicketObjs = []

i = 0
totalTickets = len(ticketNameArr)


for ticket in ticketNameArr :

    # select dropdown and press go button
    dropDownPriceOption = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/select/option[4]')))
    dropDownPriceOption.click()
    goButton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div')))
    goButton.click()

    # Click on each ticket
    ticketLink = driver.find_element(By.LINK_TEXT, ticket)
    ticketLink.click()
    # Wait for page to load 
    table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'panel-body')))

    basicInfoDiv = driver.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/div/div[1]/div[2]/div[1]')

    # remainingPrizeTableDiv = driver.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/div/div[1]/div[2]/div[2]')
    # Get table data
    # Get Top Prize


    # Get name
    ticketName = driver.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/h2')
    # Get Value
    value = basicInfoDiv.find_element(By.XPATH, './/b[4]')
    # Get Overall Odds
    odds = basicInfoDiv.find_element(By.XPATH, './/b[6]')
    # Get Game #
    gameNum = basicInfoDiv.find_element(By.XPATH, './/b[7]')
    # Remove "- number" 
    splitTicket = str(ticketName.text).split(" -", 1)
    pureTicketName = splitTicket[0]

    print()
    print('Ticket Name: ' + pureTicketName)
    print('Ticket Value: '+ value.text) 
    print('Ticket Odds: ' + odds.text)
    print('Ticket Number: ' + gameNum.text)

    singleTicket = createTicket(i, value.text, pureTicketName, odds.text, gameNum.text)
    allTicketObjs.append(singleTicket)


    print('(' + str(i+1) + '/' + str(totalTickets) +') Tickets Scrapped')
    

    i = i + 1
    driver.back()
    time.sleep(4)

print()
print("Completed Scrape!")
print("All Objects:")
print()

for ticket in allTicketObjs :
    print(ticket.ticketName + ' ' + ticket.value + ' ' + ticket.odds)



header = ['ID', 'Value', 'Name', 'Odds', 'TicketNumber']
with open('tickets.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    writer.writerow(header)

    for ticket in allTicketObjs :
        ticketArr = [ ticket.id, ticket.value, ticket.ticketName, ticket.odds, ticket.ticketNumber ]
        writer.writerow(ticketArr)
        # writer.writerow(ticket.ticketName + ' ' + ticket.value + ' ' + ticket.odds)

    


print("--- %s seconds ---" % (time.time() - start_time))

# close browser
driver.quit() 