class Node:
    """ The Node class  represents each node in the doubly linked list. It has three attributes: data to store the value
     of the node, previous as a reference to the previous node, and next as a reference to the next node."""
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
            new_node.previous = self.tail  # Set the new node's previous pointer to the current tail
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
            self.head.previous = new_node  # Update the previousious pointer of the current head to point to the new node
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

    def count_nodes(self):
        total_nodes = 0
        current = self.head
        while current is not None:
            total_nodes += 1
            current = current.next
        return total_nodes

    def remove_at_position(self, position):
        if position < 0:
            raise ValueError("Position cannot be negative.")

        if self.head is None:
            raise ValueError("The list is empty.")

        if position == 0:
            if self.head == self.tail:
                # If there is only one node in the list
                self.head = None
                self.tail = None
            else:
                # If there are more than one node in the list
                self.head = self.head.next
                self.head.previous = None
            return

        current = self.head
        count = 0

        # Traverse the list to find the node at the specified position
        while current is not None:
            if count == position:
                if current == self.tail:
                    # If removing the last node
                    self.tail = current.previous
                    self.tail.next = None
                else:
                    # If removing a node in the middle
                    current.previous.next = current.next
                    current.next.previous = current.previous
                return

            # Move to the next node
            current = current.next
            count += 1

        # If the specified position exceeds the length of the list
        raise ValueError("Position exceeds the length of the list.")

        # Add the missing return statement


# Create a new doubly linked list
my_list = DoublyLinkedList()

# Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Prepend an element
my_list.insert_at_the_beginning(90)
node_count = my_list.count_nodes()

# Print the list in forward and backward directions
print("Forward:")
my_list.print_forward()

print("Backward:")
my_list.print_backward()

print("number of nodes: ", node_count)


print("type the position the node is in to remove it: ", my_list.remove_at_position(1))

print("the amount of nodes now are: ", node_count)
