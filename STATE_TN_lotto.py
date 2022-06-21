
# scrape "https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html"

import time
from GlobalFunctions.convertTicketOddsToPercentage import convertTicketOddsToPercentage, convertTicketOddsToPercentageTN
from TN.TNHelperFunctions import *
from GlobalFunctions.sortByOdds import sortTicketsBy
from GlobalFunctions.writeToCsv import writeToCsv
from colorama import Fore
from colorama import Style

############### Setup ###############
start_time = time.time()
DRIVER
# Load website
# TNsetup()

############### MAIN ###############

# Get list of all $ amounts the website provides
dollarAmounts = ['1', '2', '3', '5', '10', '20', '25', '30']
print()

ticketList = []

for price in dollarAmounts :
    DRIVER.get(TN_LOTTERY_WEBSITE+price)
    print()
    CreateID = 1

    # Read how many tickets are displayed on the page, to know how many times to click through buttons
    count = len(DRIVER.find_elements(By.CLASS_NAME,'infoWrapper'))
    print(str(count) + ' Number of tickets found in the $' + price + ' category')


    # loop through each ticket
    for ticketIndex in range(count) :
        CreateID = CreateID + 1

        ################ Click on 'Learn More' of each ticket ###############
        path = '//*[@id="value-tax"]/section/div/div/div['+ str(ticketIndex + 1) +']/div/div[2]/button'
        buttonXPath = WAIT.until(EC.element_to_be_clickable((By.XPATH, path))).click()
        # time.sleep(1)

        ############### get the ticket name and parse into strings ###############
        name = WAIT.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[' + str(ticketIndex + 2) + ']/div/div/div[2]/h2')))
        time.sleep(1)
        ticketNameArr = (name.text).split(' #')
        ticketName = ticketNameArr[0]
        if len(ticketNameArr) == 1 :
            print(f"{Fore.RED}Could not parse ticket number...{Style.RESET_ALL}")
            ticketNumber = 0
        else :
            ticketNumber = ticketNameArr[1]
        print('Ticket name:', ticketName, 'Ticket number:', ticketNumber)

        ############### Get Odds ###############
        # NOT all ticekts are formatted with the same number of <p> tags
        oddsRaw = WAIT.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[' + str(ticketIndex + 2) + ']/div/div/div[2]/p[2]')))

        # some tickets have the odds in a list of <p> tags, loop through until the odds are found 
        x = 3
        while ('1 in ' not in oddsRaw.text) :
            oddsRaw = WAIT.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[' + str(ticketIndex + 2) + ']/div/div/div[2]/p[' + str(x) + ']')))
            x = x + 1
            if x > 10: 
                break


        oddsRaw2 = (oddsRaw.text).split('1 in ')
        odds2 = oddsRaw2[1].split('.')
        odds = odds2[0] + '.' + odds2[1]


        print('Odds are: 1 in ', odds )

        # close overlay 
        WAIT.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[' + str(ticketIndex + 2) + ']/div/div/div[2]/button/span'))).click()
        if(name) :
            print(ticketIndex + 1, name.text)
        else :
            print('Did not find Name')

        ############### Create Ticket Object and add to array ###############
        ticketObject = createTicket(CreateID, price, ticketName, odds, ticketNumber)
        ticketList.append(ticketObject)
        
        time.sleep(1)



############### Create Ticket Object and add to array ###############

print()
print("Completed Scrape!")
print("All Objects:")
print()

############### Unsorted ###############
# write unsorted to tickets.csv
writeToCsv('CSVs/TNtickets.csv', ticketList, False)

############### Sorted ###############
# sort arr of objects
sortTicketsBy(ticketList, 'odds')
# get odds in percentage
convertTicketOddsToPercentageTN(ticketList)
# write sorted to tickets.csv
writeToCsv('CSVs/TNSortedTickets.csv', ticketList, True)

print("--- %s seconds ---" % (time.time() - start_time))

# close browser
DRIVER.quit() 