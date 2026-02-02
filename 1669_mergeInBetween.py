# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
		a_node = None
		b_node = None

		counter = 0
		a -= 1
		temp = list1
		while temp.next:
			if counter == a:
				a_node = temp
			if counter == b:
				b_node = temp
			temp = temp.next
			counter += 1

		a_node.next = list2

		temp = list2
		last = None
		while temp:
			last = temp
			temp = temp.next

		a_node.next = list2
		last.next = b_node.next

		return list1


# list1 nodes
l1_0 = ListNode(10)
l1_1 = ListNode(1)
l1_2 = ListNode(13)
l1_3 = ListNode(6)
l1_4 = ListNode(9)
l1_5 = ListNode(5)

l1_0.next = l1_1
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5

list1 = l1_0  # head of list1


# list2 nodes
l2_0 = ListNode(1000000)
l2_1 = ListNode(1000001)
l2_2 = ListNode(1000002)

l2_0.next = l2_1
l2_1.next = l2_2

list2 = l2_0  # head of list2

a = 3
b = 4

head = Solution().mergeInBetween(list1, a, b, list2)


def printLinkedList(head):
	temp = head
	while temp:
		print(temp.val, end=" -> ")
		temp = temp.next


printLinkedList(head)
