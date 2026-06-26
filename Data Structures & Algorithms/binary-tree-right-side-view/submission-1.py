# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # initailize right sided queue
        rq = deque()

        # results
        res = []

        if root:
            rq.append(root)

        while rq:
            # get vals length in level
            level_len = len(rq)

            # traverse level
            for i in range(len(rq)):
                curr = rq.popleft()

                # check if rightmost val of level
                if i == level_len - 1:
                    # add to results
                    res.append(curr.val)

                #grab children
                if curr.left:
                    rq.append(curr.left)
                if curr.right:
                    rq.append(curr.right)

        # return results
        return res