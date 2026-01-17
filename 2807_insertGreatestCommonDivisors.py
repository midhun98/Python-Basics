# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            next_node = node.next
            gcd_node = ListNode(math.gcd(node.val,next_node.val))
            node.next = gcd_node
            gcd_node.next = next_node
            node = next_node
        return head