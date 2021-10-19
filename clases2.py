class Computer:

    def __init__(self):
        self.ram = ""
        self.procesor = ""

    def select_computer(self):
        op = int(input("select the desired configuration: 1-Intel , 2-AMD :"))
        options = {1: "intel", 2: "AMD"}
        selected_op = options[op]
        if selected_op == 1:
            self.ram = "16 DDR4"
            print(self.ram)
            self.procesor = "Core I7 15000x"
            print(self.procesor)
        elif selected_op == 2:
            self.ram = "16 DDR4"
            print(self.ram)
            self.procesor = "Ryzen 7 3600x"
            print(self.procesor)


c1 = Computer()
c1.select_computer()




    #selected_op = my_dict2[op](num1, num2)



