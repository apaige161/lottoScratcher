

import csv
import string


def writeToCsv(fileName: string, listOfTickets: list) :
    header = ['ID', 'Value', 'Name', 'Odds', 'TicketNumber']

    with open(fileName, 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        writer.writerow(header)

        for ticket in listOfTickets :
            # splitNumber = (ticket.odds).split(':', 1)
            # stringNumberToDivideBy = splitNumber[1]
            # #convert to float, get percentage, format string for file write
            # numberToDivideBy = float(stringNumberToDivideBy)
            # floatOdds = (1 / numberToDivideBy) * 100
            ticketOdds = format(ticket.odds, '.2f') + '%'
            ticketArr = [ ticket.id, ticket.value, ticket.ticketName, ticketOdds, ticket.ticketNumber ]
            # write to csv
            writer.writerow(ticketArr)
