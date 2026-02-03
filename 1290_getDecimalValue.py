# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        number = ''
        while current:
            number += str(current.val)
            current = current.next
        
        return int(number, 2)