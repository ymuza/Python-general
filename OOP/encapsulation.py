"""
encapsulation is the building of data, along with the methods that operate that data
into a single unit (generally a class). No one can access the data inside the class, from
the outside of the class, so we can restrict the access. This prevents data inside
the class from being modified.
"""


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def set_max_price(self, price):
        self.__maxprice = price


c = Computer()  # c is the object created from the Computer class.
c.sell()

# change the price
c.__maxprice = 1000  # this won't work, because of encapsulation.
c.sell()

# using setter function
c.set_max_price(1000)  # in order to change the max price, the only way is to use a setter function
c.sell()




