# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Workspace in Solution class
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # assign head to curr
        curr, prev = head, None

        # while a curr exist
        while curr:
            temp = curr.next    # place holder for original next node
            curr.next = prev    # reassign link
            prev = curr         # assign prev to curr 
            curr = temp         # assign  cuur to next original node(temp)

        # return prev
        return prev     # (curr is None, prev is the last element visited)