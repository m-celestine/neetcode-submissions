# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        traverse = []

        def inorder(node):
            # base case
            if not node:
                return

            # get lowest number first
            inorder(node.left)
            # append to list 
            traverse.append(node.val)
            #scan right side of node
            inorder(node.right)


        inorder(root)

        #return kth(k - 1) num
        return traverse[k-1]
