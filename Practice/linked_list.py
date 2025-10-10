class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_beginning(self, data):
        nb = Node(data)
        if self.head:
            nb.next = self.head
        self.head = nb

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert_beginning(10)
ll.insert_beginning(5)
ll.insert_beginning(2)
ll.print_list()  # Outputs: 2 -> 5 -> 10 -> None