# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if empty
        if not root:
            root = TreeNode(val)

        
        # check left side or root
        if  val < root.val:
            # check if there not children
            if not root.left:
                root.left = TreeNode(val)
            #if children go to leftt child
            else:
                self.insertIntoBST(root.left, val)

        # check right side or root
        elif  val > root.val:
            # check if there not children
            if not root.right:
                root.right = TreeNode(val)
            #if children go to right child
            else:
                self.insertIntoBST(root.right, val)

        return root
        
