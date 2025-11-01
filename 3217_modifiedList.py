from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
		remove_set = set(nums)

		# Step 1: skip initial nodes that should be removed
		while head and head.val in remove_set:
			head = head.next

		# Step 2: use a temp pointer to traverse the rest
		temp = head
		while temp and temp.next:
			if temp.next.val in remove_set:
				temp.next = temp.next.next
			else:
				temp = temp.next

		return head


# Helper function to build a linked list from Python list
def build_linked_list(values: list[int]) -> Optional[ListNode]:
	if not values:
		return None
	head = ListNode(values[0])
	current = head
	for val in values[1:]:
		current.next = ListNode(val)
		current = current.next
	return head

# Helper function to print a linked list
def print_linked_list(head: Optional[ListNode]):
	result = []
	while head:
		result.append(head.val)
		head = head.next
	print(result)


# ---- Test ----
ss = Solution()
nums = [1, 2, 3]
head = build_linked_list([1, 2, 3, 4, 5])

new_head = ss.modifiedList(nums, head)
print_linked_list(new_head)   # Output: [4, 5]
