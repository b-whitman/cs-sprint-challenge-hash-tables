#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticket_dict = {ticket.source: ticket.destination for ticket in tickets}
    start = ticket_dict['NONE']
    route = [start]
    curr = start
    next = ticket_dict[start]

    while curr != 'NONE':
        curr = next
        route.append(curr)
        next = ticket_dict[curr]

    return route