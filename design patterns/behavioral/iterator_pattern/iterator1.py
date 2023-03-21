"""In this pattern, the objective is to go through an object without exposing
 the implementation of the collection"""


class Iterator1:
    def __init__(self, my_list):
        self.index = 0
        self.example_list = my_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.example_list):
            raise StopIteration
        value = self.example_list[self.index]
        self.index += 1
        return value


example_list = [1, 2, 3, 4, 5]
my_iterator = Iterator1(example_list)

for item in my_iterator:
    print(item)
