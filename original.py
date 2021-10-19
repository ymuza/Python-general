class Node:

    def __init__(self, data=None):
        self.data=data
        self.next=None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.root=None
        self.last=None


    def append_val(self, x):
        if self.root==None:
            self.root=x
        else:
            self.last.next=x
        self.last=x



    def __str__(self):
        to_print=""
        current=self.root
        while current is not None:
            to_print=to_print + str(current.data) + "->"
            current=current.next
        return to_print

    def add_to_start(self, x):
        if self.root is not None:
            self.root=x
            return x




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


node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
my_list=LinkedList()

my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)
print (my_list)
