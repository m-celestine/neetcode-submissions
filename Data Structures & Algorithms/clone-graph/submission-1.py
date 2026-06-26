"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # map old node to new nodes
        old_to_new = {}

        # dfs
        def dfs(node):
            # check if in hash
            if node in old_to_new:
                return old_to_new[node]

            # create clone/copy 
            copy = Node(node.val)
            # add copy to hash map
            old_to_new[node] = copy

            # make copys of neighbors
            for neighbor in node.neighbors:
                # add to copy's list of neighbors, the return statement from the neighbor's dfs
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else None