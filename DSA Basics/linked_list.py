"""
The code defines a singly linked list with a Node class and a LinkedList class that can display the
elements in the list.

The line `print(type(temp))` in the `display` method of the `SLinkedList` class is printing the type
of the current node `temp`. It is used to show that `temp` is an instance of the `Node` class.

"""


class Node:
    def __init__(self, data=None):
        self.data = data  # The data part of the node
        self.next = None  # Pointer to the next node


class SLinkedList:
    def __init__(self):
        self.head = None  # Points to the first node of the linked list

    def insert_begining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_position(self, pos, data):
        np = Node(data)
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        np.next = temp.next
        temp.next = np

    def display(self):
        if self.head is None:
            return "Linked list is empty"
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next


L = SLinkedList()
n1 = Node(10)
L.head = n1

n2 = Node(20)
# L.head.next = n2
n1.next = n2  #  linking n1 to n2

n3 = Node(30)
# L.head.next.next = n3
n2.next = n3  # linking n2 to n3


L.insert_begining(5)
L.insert_end(40)
L.insert_position(4, 20)
L.display()
