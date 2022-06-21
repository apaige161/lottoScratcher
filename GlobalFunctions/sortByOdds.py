# sort by odds

from audioop import reverse
import string
from operator import attrgetter
from ticketClass import Ticket

def sortTicketsBy(object: Ticket, field : string) :
    object.sort(key=attrgetter(field), reverse=False)