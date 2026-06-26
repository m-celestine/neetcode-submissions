# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stack to store traversal order
        stack = []

        def inorder(node):
            # base case
            if not node:
                return

            #traverse left side
            inorder(node.left)
            #store order val in stack
            stack.append(node.val)
            # teaverse right side
            inorder(node.right)
        
        # get order
        inorder(root)

        #return inorder traversal vals
        return stack