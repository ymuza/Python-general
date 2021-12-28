class Cars:

    def __init__(self, make: str, year: int, engine: str, km: int):
        self.make = make
        self.year = year
        self.engine = engine
        self.km = km
        self.serv = False

    def service(self) -> bool:
        op = (input("does the car have the latest service done (y/n)? "))
        if op == 'y':
            self.serv = True
        elif op == 'n':
            self.serv = False
        return self.serv

    def usage(self):
        if self.km < 80000 and self.serv is True:
            print("The car does not need maintenance.")
        else:
            print("you need to perform maintenance.")

    @staticmethod
    def taxes():
        tax_checker = 10
        if tax_checker <= 10:
            print("The car doesn't pay taxes.")


c = Cars((input("type the maker: ")),
         int((input("type the year: "))),
         input("type engine model: "),
         int((input("type amount of kms: "))))

c.service()
c.usage()
c.taxes()
