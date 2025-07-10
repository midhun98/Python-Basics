from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		head = ListNode()  # dummy node
		temp = head  # temp acts like a moving pointer

		while list1 and list2:
			if list1.val < list2.val:
				temp.next = list1
				list1 = list1.next
			else:
				temp.next = list2
				list2 = list2.next
			temp = temp.next  # move to the next node

		if list1:
			temp.next = list1
		else:
			temp.next = list2
		return head.next  # return the actual start, skipping the dummy


def build_linked_list(values):
	returnNode = ListNode()
	head = returnNode
	for val in values:
		head.next = ListNode(val)
		head = head.next
	return returnNode.next


def print_linked_list(head):
	result = []
	while head:
		result.append(head.val)
		head = head.next
	print(result)


ss = Solution()
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])
merged = ss.mergeTwoLists(list1, list2)
print_linked_list(merged)  # Output: [1, 1, 2, 3, 4, 4]

while list1:
	print(list1.val)
	list1 = list1.next
