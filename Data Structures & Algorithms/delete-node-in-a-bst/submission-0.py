# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return root

        # bst to find node
        # check left side
        if key < root.val:
            #check left side
            root.left = self.deleteNode(root.left, key)
        # check right side
        elif key > root.val:
            #check left side
            root.right = self.deleteNode(root.right, key)

        # delete and rearrange
        else:
            #if only right
            if not root.left:
                return root.right
            #if only left
            elif not root.right:
                return root.left

            #
            curr = root.right
            while curr.left:
                curr = root.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)

        # return Tree
        return root
            
            



