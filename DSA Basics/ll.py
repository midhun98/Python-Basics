class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

def printLL(head):
    temp = head
    while temp:
        print(temp.value, "-->")
        temp = temp.next

printLL(first)