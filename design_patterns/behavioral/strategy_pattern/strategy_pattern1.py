"""Strategy pattern (class based): the customer support app delegates the order in
which tickets are processed to an interchangeable strategy object."""

import string
import random
from abc import ABC, abstractmethod


def generate_id(length=8):
    """generates a random id of uppercase letters"""
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    """a customer support ticket with a random id"""

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketOrderingStrategy(ABC):
    """strategy interface: decides in which order the tickets are processed"""
    @abstractmethod
    def create_ordering(self, lista: list[SupportTicket]) -> list[SupportTicket]:
        """returns the tickets in the order they should be processed"""


class FIFOOrderingStrategy(TicketOrderingStrategy):
    """processes tickets in the order they were created"""
    def create_ordering(self, lista: list[SupportTicket]) -> list[SupportTicket]:
        return lista.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    """processes the newest tickets first"""
    def create_ordering(self, lista: list[SupportTicket]) -> list[SupportTicket]:
        list_copy = lista.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    """processes tickets in random order"""
    def create_ordering(self, lista: list[SupportTicket]) -> list[SupportTicket]:
        list_copy = lista.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleStrategy(TicketOrderingStrategy):
    """discards every ticket, nothing gets processed"""
    def create_ordering(self, lista: list[SupportTicket]) -> list[SupportTicket]:
        return []


class CustomerSupport:
    """the context: holds the tickets and delegates their ordering to a strategy"""

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        """orders the tickets with the current strategy and processes them"""
        # create the ordered list
        ticket_list = self.processing_strategy.create_ordering(self.tickets)

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


if __name__ == "__main__":
    # create the application
    app = CustomerSupport(RandomOrderingStrategy())

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    # process the tickets
    app.process_tickets()
