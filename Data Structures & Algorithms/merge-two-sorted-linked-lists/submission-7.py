# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        comb_list = curr = ListNode()

        while list1 and list2:
            #
            if list1.val < list2.val:
                # link curr comb_list node to curr list1 node
                curr.next = list1
                # reassign list1 node to next node of list1
                list1 = list1.next
            #
            else:
                # link curr comb_list node to curr list2 node
                curr.next = list2
                # reassign list2 node to next node of list2
                list2 = list2.next
            # reassign curr comb_list node to next node of comb_list
            curr = curr.next

        curr.next = list1 or list2
        
        return comb_list.next