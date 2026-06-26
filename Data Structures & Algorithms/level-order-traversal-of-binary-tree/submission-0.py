# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #initialize queue
        queue = deque()

        # holder for results
        res = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            # make list of values in current level
            level_vals = []
            # get breath for curr level
            for i in range(len(queue)):
                # get node from queue
                curr = queue.popleft()
                #add curr val  to level list
                level_vals.append(curr.val)

                #add children to queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            # add list of vals from level to results list
            res.append(level_vals)

        # return list of lists
        return res
