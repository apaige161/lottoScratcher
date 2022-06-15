


# constructor
class Ticket(object) :
    id = ""
    ticketName = ""
    odds = ""
    ticketNumber = 0

    # initialize 
    def __init__(self, id, value, ticketName, odds, ticketNumber) :
        self.id = id
        self.value = value
        self.ticketName = ticketName
        self.odds = odds
        self.ticketNumber = ticketNumber

def createTicket(id, value, ticketName, odds, ticketNumber) :
    ticket = Ticket(id, value, ticketName, odds, ticketNumber)
    return ticket
