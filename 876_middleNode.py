from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow


ss = Solution()
head = [1,2,3,4,5]

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

head = list_to_linked_list(head)

ss.middleNode(head)