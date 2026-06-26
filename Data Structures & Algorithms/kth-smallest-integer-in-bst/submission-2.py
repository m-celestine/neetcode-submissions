# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.traverse = []

        self.inorder(root)

        #return kth(k - 1) num
        return self.traverse[k-1]

    def inorder(self, node):
            # base case
            if not node:
                return

            # get lowest number first
            self.inorder(node.left)
            # append to list 
            self.traverse.append(node.val)
            #scan right side of node
            self.inorder(node.right)