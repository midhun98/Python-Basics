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

	def insert_beginning(self, data):
		nb = Node(data)  # nb - node beginning
		nb.next = self.head  # set the next of the new to the head
		self.head = nb  # make the new node as head

	def insert_end(self, data):
		ne = Node(data)  # ne - node end
		temp = self.head  # assign the head to temp
		while temp.next:  # loop until next is null
			temp = temp.next  # assign the last node to temp
		temp.next = ne  # assign the last next of temp to ne

	def insert_position(self, pos, data):
		np = Node(data)
		temp = self.head

		if pos == 1:
			np.next = self.head
			self.head = np
			return

		for i in range(pos - 1):
			if temp is None:
				raise IndexError("Position out of bounds")
			temp = temp.next
			print("Inserting after:", temp.data)

		if temp is None:
			raise IndexError("Position out of bounds")

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
L.insert_beginning(4)
L.insert_end(8)
L.insert_end(15)
L.insert_end(16)
L.insert_position(2, 10)
L.display()

# First will be the head
'''
using first we can access all the next ones
'''
first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

print('\n')
print(first.data)
print(first.next.data)
print(first.next.next.data)
