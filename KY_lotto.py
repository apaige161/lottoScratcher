
# scrape "https://www.kylottery.com/apps/scratch_offs/prizes_remaining.html"

import time
from convertTicketOddsToPercentage import convertTicketOddsToPercentage
from KY.kyHelperFunctions import *
from sortByOdds import sortTicketsBy
from writeToCsv import writeToCsv

############### Setup ###############
start_time = time.time()
DRIVER
JSON_file = "./ticketData.json"
# Load website
KYsetup()
# Wait for item to be clickable then go to page for data collection
selectDropDownSelectPriceOptionSelectGo()

############### MAIN ###############
# Get each price point
getListOfTicketValues()

# Get all ticket names
ticketNameArr = []
tickets = getListOfTicketNames()

for ticket in tickets:
    #add ticket text only to new array
    ticketNameArr.append(ticket.text)

print("Number of tickets found: " + str(len(tickets)))

printListOfTickets(ticketNameArr)

print("start loop iteration")


allTicketObjs = []

i = 0
for ticket in ticketNameArr :
    # select dropdown and press go button
    selectDropDownSelectPriceOptionSelectGo()
    # Click on each ticket
    basicInfoDiv = clickTicket(ticket)
    # Collect relavent ticket data
    print('(' + str(i+1) + '/' + str(len(tickets)) +') Tickets Scrapped')
    getTicketData(i, basicInfoDiv, allTicketObjs)
    
    i = i + 1
    DRIVER.execute_script("window.history.go(-1)")
    time.sleep(4)

print()
print("Completed Scrape!")
print("All Objects:")
print()

############### Unsorted ###############
# write unsorted to tickets.csv
writeToCsv('CSVs/KYtickets.csv', allTicketObjs, False)

############### Sorted ###############
# sort arr of objects
sortTicketsBy(allTicketObjs, 'odds')
# get odds in percentage
convertTicketOddsToPercentage(allTicketObjs)
# write sorted to tickets.csv
writeToCsv('CSVs/KySortedTickets.csv', allTicketObjs, True)

print("--- %s seconds ---" % (time.time() - start_time))

# close browser
DRIVER.quit() 