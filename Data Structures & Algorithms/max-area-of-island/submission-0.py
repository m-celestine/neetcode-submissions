class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # empty case
        if not grid:
            return 0

        # get rows and cols
        rows, cols = len(grid), len(grid[0])

        # tracker for visited paths
        visit = set()
        # track island with max area
        max_island = 0
        

        def dfs (r, c):
            # base case
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visit:
                return 0             

            # add path to visit
            visit.add((r,c))

            # search island     # track the area of island
            return (1 + dfs(r - 1, c) +
                        dfs(r + 1, c) +
                        dfs(r, c - 1) +
                        dfs(r, c + 1))       
                
            
        # search matrix
        for row in range(rows):
            for col in range(cols):
                # update tracker for area of current island
                curr_area = 0

                if grid[row][col] == 1 and (row, col) not in visit:
                    curr_area = dfs(row, col)

                if curr_area > max_island:
                    max_island = curr_area

        # return max area of islands
        return max_island
            
