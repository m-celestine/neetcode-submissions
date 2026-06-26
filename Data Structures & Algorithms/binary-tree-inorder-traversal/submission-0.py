# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 
    def inorder(self, node, stack):
            # base case
            if not node:
                return

            #traverse left side
            self.inorder(node.left, stack)
            #store order val in stack
            stack.append(node.val)
            # teaverse right side
            self.inorder(node.right, stack)
    
    # main function
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stack to store traversal order
        stack = []
        
        # get order
        self.inorder(root, stack)

        #return inorder traversal vals
        return stack