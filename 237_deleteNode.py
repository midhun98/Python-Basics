# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val  # 
        node.next = node.next.next
        


# Create nodes
n1 = ListNode(4)
n2 = ListNode(5)
n3 = ListNode(1)
n4 = ListNode(9)

# Link them
n1.next = n2
n2.next = n3
n3.next = n4

head = n1        # head = 4
node = n2        # node to delete = 5


Solution().deleteNode(node)
