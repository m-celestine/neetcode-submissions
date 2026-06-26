class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # get amount of paths
        paths = self.dfs(grid, 0, 0, set())

        # return amount of paths discovered
        return paths

        

    #DFS Function
    def dfs(self, grid, r, c, visit):
        # get bounds for rows and cols
        ROWS, COLS = len(grid), len(grid[0])

        # edge cases  ->  bounds, then visited, last blocked
        if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1:
            return 0

        # case for end of routes
        if r == ROWS - 1 and  c == COLS - 1:
            return 1


        # mark path as visit
        visit.add((r, c))

        # traversal tracker
        routes = 0
        # recursions  -> r: up, down. c: left, right
        routes += self.dfs(grid, r - 1, c, visit)
        routes += self.dfs(grid, r + 1, c, visit)
        routes += self.dfs(grid, r, c - 1, visit)
        routes += self.dfs(grid, r, c + 1, visit)

        # remove path from visit as we back track
        visit.remove((r, c))

        # return amount of routes discovered
        return routes



