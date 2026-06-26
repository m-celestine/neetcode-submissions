# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if empty or no children
        if not root:
            return TreeNode(val)

        
        # check left side or root
        if  val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        # check right side or root
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root
        
