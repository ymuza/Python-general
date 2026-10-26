"""Strategy pattern (functional version): instead of strategy classes, each ordering
strategy is a plain function that is passed to process_tickets."""

from dataclasses import dataclass, field
import string
import random
from collections.abc import Callable


def generate_id(length: int = 8) -> str:
    """generates a random id of uppercase letters"""
    return ''.join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    """a customer support ticket, the id is generated automatically"""
    customer: str
    issue: str
    id: str = field(init=False, default_factory=generate_id)


type SupportTickets = list[SupportTicket]

Ordering = Callable[[SupportTickets], SupportTickets]


def fifo_ordering(lista: SupportTickets) -> SupportTickets:
    """processes tickets in the order they were created"""
    return lista.copy()


def filo_ordering(lista: SupportTickets) -> SupportTickets:
    """processes the newest tickets first"""
    list_copy = lista.copy()
    list_copy.reverse()
    return list_copy


def random_ordering(lista: SupportTickets) -> SupportTickets:
    """processes tickets in random order"""
    list_copy = lista.copy()
    random.shuffle(list_copy)
    return list_copy


def blackhole_ordering(_: SupportTickets) -> SupportTickets:
    """discards every ticket, nothing gets processed"""
    return []


class CustomerSupport:
    """holds the tickets, the ordering strategy is passed in when processing"""

    def __init__(self):
        self.tickets: SupportTickets = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, ordering: Ordering):
        """orders the tickets with the given strategy function and processes them"""
        # create the ordered list
        ticket_list = ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    @staticmethod
    def process_ticket(ticket: SupportTicket):
        """prints the details of a single ticket"""
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


def main() -> None:
    """registers a few tickets and processes them in random order"""
    # create the application
    app = CustomerSupport()

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian",
                      "I can't upload any videos, please help.")
    app.create_ticket(
        "Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    # process the tickets
    app.process_tickets(random_ordering)


if __name__ == '__main__':
    main()
