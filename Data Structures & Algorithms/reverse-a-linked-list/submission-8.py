# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Workspace in Solution class
class Solution:         # Factorial Solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head:
            return None
        
        # recursive case
        # initailize return node/list
        new_head = head

        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head

        # point head to null
        head.next = None

        return new_head
