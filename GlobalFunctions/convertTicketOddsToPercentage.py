

def convertTicketOddsToPercentage(listOfTickets: list) :
    for ticket in listOfTickets :
        splitNumber = (ticket.odds).split(':', 1)
        stringNumberToDivideBy = splitNumber[1]
        #convert to float, get percentage, format string for file write
        numberToDivideBy = float(stringNumberToDivideBy)
        ticket.odds = (1 / numberToDivideBy) * 100

def convertTicketOddsToPercentageTN(listOfTickets: list) :
    for ticket in listOfTickets :
        #convert to float, get percentage
        numberToDivideBy = float(ticket.odds)
        ticket.odds = (1 / numberToDivideBy) * 100