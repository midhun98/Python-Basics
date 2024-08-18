class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            return "Linked list is empty"
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next


L = SLinkedList()
n1 = Node(10)
L.head = n1

n2 = Node(20)
n1.next = n2  #  linking n1 to n2

n3 = Node(30)
n2.next = n3  # linking n2 to n3

L.display()
