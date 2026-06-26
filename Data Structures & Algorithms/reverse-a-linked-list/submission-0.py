# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Create variables prev and curr
        prev = None
        curr = head

        while curr:     # while curr is not null
            #store curr.next (next node)
            temp = curr.next
            #prev become the new next
            curr.next = prev
            
            prev = curr   #prev become the curr node
            curr = temp   #curr node becomes the orignal next node

        #return
        return prev

