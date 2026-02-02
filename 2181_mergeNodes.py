from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
		new_head = None
		tail = None
		curr_sum = 0
		current = head

		while current:
			if current.val == 0 and curr_sum != 0:
				new_node = ListNode(curr_sum)

				# core logic starts
				if new_head is None:
					new_head = new_node
					tail = new_node
				else:
					tail.next = new_node
					tail = new_node
				# core logic ends

				curr_sum = 0
			else:
				curr_sum += current.val
			current = current.next
		return new_head


head = [0, 1, 0, 3, 0, 2, 2, 0]


def list_to_linked_list(arr):
	if not arr:
		return None
	head = ListNode(arr[0])
	current = head
	for i in range(1, len(arr)):
		new_node = ListNode(arr[i])
		current.next = new_node
		current = new_node

	return head


ll = list_to_linked_list(head)


def printLinkedList(head):
	temp = head
	while temp:
		print(temp.val, end=" -> ")
		temp = temp.next


# printLinkedList(ll)


head = Solution().mergeNodes(ll)
printLinkedList(head)
