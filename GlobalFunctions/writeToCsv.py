

import csv
import string


def writeToCsv(fileName: string, listOfTickets: list, fomattedToPercentage: bool) :
    header = ['ID', 'Value', 'Name', 'Odds', 'TicketNumber']

    with open(fileName, 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        writer.writerow(header)

        for ticket in listOfTickets :
            if fomattedToPercentage :
                ticketOdds = format(ticket.odds, '.2f') + '%'
            else :
                ticketOdds = ticket.odds
            ticketArr = [ ticket.id, ticket.value, ticket.ticketName, ticketOdds, ticket.ticketNumber ]
            print(ticketArr)
            # write to csv
            writer.writerow(ticketArr)
