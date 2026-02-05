# Definition for singly-linked list.
from posixpath import curdir
from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
		while head and head.val == val:
			head = head.next

		current = head
		while current and current.next:
			if current.next.val == val:
				current.next = current.next.next
			else:
				current = current.next
		return head


head = [7, 7, 8, 7, 7]
val = 7
ss = Solution()


def create_ll(li):
	head = ListNode(li[0])
	current = head
	for i in range(1, len(li)):
		new_node = ListNode(li[i])
		current.next = new_node
		current = new_node
	return head


head = create_ll(head)

header = ss.removeElements(head, val)


def print_ll(head):
	current = head
	while current:
		print(current.val)
		current = current.next


print_ll(header)
