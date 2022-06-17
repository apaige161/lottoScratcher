


# currently not used but saving it for later

def convertTicketOddsToPercentage(listOfTickets: list) :
    for ticket in listOfTickets :
        splitNumber = (ticket.odds).split(':', 1)
        stringNumberToDivideBy = splitNumber[1]
        #convert to float, get percentage, format string for file write
        numberToDivideBy = float(stringNumberToDivideBy)
        ticket.odds = (1 / numberToDivideBy) * 100
