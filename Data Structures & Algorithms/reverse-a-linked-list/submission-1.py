# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Workspace in Solution class
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # store linked list in array
        array = []
        # while a head exist
        while head:
            # add current head value to array
            array.append(head.val)
            #move head to next link
            head = head.next
        
        # array
        array.reverse()

        # make reversed array new linked list
        for num in array:
            # turn num into a node vl
            new = ListNode(num)

            # check if we have a head pointer
            if not head:
                head = new
                #initialize a tracker for linked list
                current = head
                continue
            #current point to num (add num to the list)
            current.next = new
            # num become new current
            current = current.next

        # return new linked list
        return head
