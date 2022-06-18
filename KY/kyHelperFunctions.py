
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException

from ticketClass import createTicket


options = webdriver.ChromeOptions()
PATH = "C:/Program Files (x86)/chromedriver.exe"
DRIVER = webdriver.Chrome(PATH)
KYLotteryWebsite = 'https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html'

wait = WebDriverWait(DRIVER, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

# Load website
# 
def KYsetup():
    DRIVER.get(KYLotteryWebsite)

def selectDropDownSelectPriceOptionSelectGo():
    # select dropdown and press go button
    dropDownPriceOption = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/select/option[4]')))
    dropDownPriceOption.click()
    goButton = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div')))
    goButton.click()

def getListOfTicketValues():
    pricesArray = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "klc-scratch-price_section")))
    for prices in pricesArray:
        print(prices.text)
    
# returns a list of strings (tickets) 
def getListOfTicketNames():
    return DRIVER.find_elements(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div[2]/div[3]/div[2]/div[2]/ul/li/a')
    

def printListOfTickets(ticketList: list):
    for ticket in ticketList:
        print("Ticket Name: " + ticket)

def clickTicket(ticket):
    ticketLink = DRIVER.find_element(By.LINK_TEXT, ticket)
    ticketLink.click()
    # Wait for page to load 
    table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'panel-body')))
    return DRIVER.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/div/div[1]/div[2]/div[1]')

def getTicketData(index, ticketDiv, listToAppend):
    # Get name
    ticketName = DRIVER.find_element(By.XPATH, '//*[@id="snapContent"]/div[5]/div/div/div/div/div[4]/div/h2')
    # Get Value
    value = ticketDiv.find_element(By.XPATH, './/b[4]')
    # Get Overall Odds
    odds = ticketDiv.find_element(By.XPATH, './/b[6]')
    # Get Game #
    gameNum = ticketDiv.find_element(By.XPATH, './/b[7]')
    # Remove "- number" 
    splitTicket = str(ticketName.text).split(" -", 1)
    pureTicketName = splitTicket[0]

    
    print('Ticket Name: ' + pureTicketName)
    print('Ticket Value: '+ value.text) 
    # print('Ticket Odds: ' + odds.text)
    # print('Ticket Number: ' + gameNum.text)
    print()

    singleTicket = createTicket(index, value.text, pureTicketName, odds.text, gameNum.text)
    listToAppend.append(singleTicket)
