class Graph:
    
    def __init__(self):
        self.adjLst = {}    # src maps to set of neighbors


    def addEdge(self, src: int, dst: int) -> None:
        # add to hash if not in list already
        if src not in self.adjLst:
            self.adjLst[src] = set()    # use set for O(1) checks
        if dst not in self.adjLst:
            self.adjLst[dst] = set()    # list would have O(n) "in" checks
        # add edge to list of neighbors
        self.adjLst[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjLst or dst not in self.adjLst[src]:
            return False
        # remove edge
        self.adjLst[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        # initialize visited variable
        visited = set()
        # check for path to target 
        path = self.dfs(src, dst, visited)
        # return if path was found
        return path


    def dfs(self, src, dst, visited):
        # return True if path found
        if src == dst:
            return True
        
        # add current node to visited
        visited.add(src)

        # loop neighbors to find target destination
        for neighbor in self.adjLst.get(src, set()):
            # neighbor has not been visited
            if neighbor not in visited:
                # check neighbor for a path
                if self.dfs(neighbor, dst, visited):
                    return True
        
        # no route found
        return False
