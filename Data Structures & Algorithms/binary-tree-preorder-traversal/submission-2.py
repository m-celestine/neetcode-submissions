# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # init res to track path
        res = []

        # preorder: val, left, right
        def preorder(root):
            # empty case
            if not root:
                return

            # add to res (possible because inside same function)
            res.append(root.val)
            # traverse left
            preorder(root.left)
            # traverse right
            preorder(root.right)

        # call preorder func
        preorder(root)
        # return res
        return res



    