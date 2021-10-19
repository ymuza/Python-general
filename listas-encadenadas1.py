class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:

    def __init__(self):
        self.root = None
        self.last = None

    def append_val(self, x):
        if self.root is None:
            self.root = x
        else:
            self.last.next = x
        self.last = x

    def __str__(self):
        to_print = ""
        current = self.root
        while current is not None:
            to_print = to_print + str(current.data) + "->"
            current = current.next
        if to_print:
            return "[" + to_print[:-2] +"]"
        return "[]"

    def amount_of_nodes(self):
        amount = 0
        scroller = self.root
        while scroller is not None:
            scroller = scroller.next
            amount = amount+1

        print(amount)

    def add_to_start(self,x):
        pass

    def search_val(self, x):
        '''return indices where x was found'''
        pass

    def remove_val_by_index(self, x):
        '''remove and return value at index x provided as parameter'''
        pass

    def length(self):
        '''return the length of the list, rep'd by number of nodes'''
        pass

    def reverse_list_recur(self, current, previous):
        '''reverse the sequence of node pointers in the linked list'''
        pass


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

my_list = LinkedList()

print("select an operation (1-see appended values, 2-add node to the beginning of the list, 3-search for a node, 4-remove node from list, 5-show the list length, 6-reverse the list recursively ): ")
op = int(input())


my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)


if op == 1:
    print(my_list)

if op == 2:
    node0 = Node(9)
    my_list.add_to_start(node0)
    print(my_list)

#    my
if op == 5:
    my_list.amount_of_nodes()
    print(my_list)
