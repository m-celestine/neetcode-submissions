class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # empty case
        if not grid:
            return 0

        # get rows and columns
        rows, cols = len(grid), len(grid[0])

        # tracker for visited and islands
        visit = set()
        islands = 0


        # dfs to explore island and mark it
        def dfs(r, c):
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visit:
                return

            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            # mark current location to visit
            visit.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)



        # traverse to find islands
        for r in range(rows):
            for c in range(cols):
                # if new island found, traverse it
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
                
        # return number of islands
        return islands