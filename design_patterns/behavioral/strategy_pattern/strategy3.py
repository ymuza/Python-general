"""Strategy pattern with plain functions: an Item stores a reference to a discount
strategy (a function) and delegates the discount calculation to it. Adding a new type
of discount means adding a new function, not changing Item. Our Item class only knows
that the strategy takes the item and returns the discount amount."""


# A separate class for Item
class Item:
    """An item with a price and an optional discount strategy"""

    def __init__(self, price, discount_strategy=None):
        """take price and discount strategy_pattern"""
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        """A separate function for price after discount"""

        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self):

        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"


def on_sale_discount(item):
    """function dedicated to On Sale Discount"""
    return item.price * 0.25 + 20


def twenty_percent_discount(item):
    """function dedicated to 20 % discount"""
    return item.price * 0.20


# main function
if __name__ == "__main__":
    print(Item(20000))

    # with discount strategy_pattern as 20 % discount
    print(Item(20000, discount_strategy=twenty_percent_discount))

    # with discount strategy_pattern as On Sale Discount
    print(Item(20000, discount_strategy=on_sale_discount))
