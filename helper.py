
import json
from ticketClass import Ticket

tester = {"id": 0, "ticketName": "10X", "odds": "1:4.87", "ticketNumber": "772"}


def encoder_ticket(ticket : Ticket):
        return { 
            'id' : ticket.id, 
            'value': ticket.value,
            'ticketName' : ticket.ticketName, 
            'odds' : ticket.odds, 
            'ticketNumber' : ticket.ticketNumber
        }

jsonified_ticket = json.dumps(tester, default=encoder_ticket)
print()
print(jsonified_ticket)