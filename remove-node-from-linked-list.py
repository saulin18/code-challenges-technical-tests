# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has 
# Node.val == val, and return the new head.
# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:
# Input: head = [], val = 1
# Output: []
# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []
# Constraints:
#     The number of nodes in the list is in the range [0, 104].
#     1 <= Node.val <= 50
#     0 <= val <= 50

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None: 

        while head is not None and head.val == val:
            head = head.next if head.next is not None else None

        if head is None:
            return head
        
        if head.next is None:
            return head if head.val != val else None
        
        curr = head
        while curr.next is not None:
            next: ListNode = curr.next
            if next is None:
                break
            if next.val == val:
                curr.next = next.next if next.next is not None else None
            else:
                curr = curr.next

        return head