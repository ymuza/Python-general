class Node:
    """ The Node class  represents each node in the doubly linked list. It has three attributes: data to store the value
     of the node, prev as a reference to the previous node, and next as a reference to the next node."""
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # the head points to None
        self.tail = None  # the tail also points to None

    def append(self, data):
        """adds a new node to the list"""
        new_node = Node(data)

        if self.head is None:  # if the list is empty, the new node becomes the head and tail
            self.head = new_node
            self.tail = new_node
        else:  # If the list is not empty:
            new_node.previous = self.tail  # Set the new node's prev pointer to the current tail
            self.tail.next = new_node  # Update the next pointer of the current tail to point to the new node
            self.tail = new_node  # Update the tail to the new node

    def insert_at_the_beginning(self, data):
        # If the list is empty, make the new node the head and tail
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty
            new_node.next = self.head  # Set the new node's next pointer to the current head
            self.head.previous = new_node  # Update the prev pointer of the current head to point to the new node
            self.head = new_node  # Update the head to the new node

    def print_forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def print_backward(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.previous


# Create a new doubly linked list
my_list = DoublyLinkedList()

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Prepend an element
my_list.insert_at_the_beginning(90)

# Print the list in forward and backward directions
print("Forward:")
my_list.print_forward()

print("Backward:")
my_list.print_backward()

