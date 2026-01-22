from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		li = []
		temp = head

		while temp:
			li.append(temp.val)
			temp = temp.next

		return li == li[::-1]


def build_linked_list(arr):
	dummy = ListNode()
	curr = dummy
	for x in arr:
		curr.next = ListNode(x)
		curr = curr.next
	return dummy.next


head = build_linked_list([1, 2, 2, 1])

ss = Solution()
print(ss.isPalindrome(head))  # True
