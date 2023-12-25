class Cars:

    def __init__(self, vehicle_info):
        self.make = vehicle_info[0]
        self.year = vehicle_info[1]
        self.engine = vehicle_info[2]
        self.km = vehicle_info[3]
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


maker: str = input("Type the maker: ")
year: int = int(input("type the year: "))
engine_model: str = input("type engine model: ")
km: int = int(input("type amount of kms: "))

VehicleInfo = [maker, year, engine_model, km]
c = Cars(VehicleInfo)

c.service()
c.usage()
c.taxes()
