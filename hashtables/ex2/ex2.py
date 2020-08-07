#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_cache = {}
    route = []

    for ticket in tickets:
        if ticket.source not in ticket_cache:
            ticket_cache[ticket.source] = ticket.destination

    cur = ticket_cache["NONE"]
    while cur is not "NONE":
        route.append(cur)
        cur = ticket_cache[cur]

    route.append(cur)

    return route

if __name__ == "__main__":
    ticket_1 = Ticket("NONE", "PDX")
    ticket_2 = Ticket("PDX", "DCA")
    ticket_3 = Ticket("DCA", "NONE")

    tickets = [ticket_1, ticket_2, ticket_3]
    print(reconstruct_trip(tickets, 3))