# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # init trav to track path
        trav = []

        # preorder: val, left, right
        def preorder(root, path):
            # empty case
            if not root:
                return []
            # add to path
            path.append(root.val)
            # traverse left
            preorder(root.left, path)
            # traverse right
            preorder(root.right, path)

            # return path
            return path

        res = preorder(root, trav)

        return res



    