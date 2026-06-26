from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # get length of rows and columns
        rows, cols = len(grid), len(grid[0])

        # initialize queue for bfs and visited tracker
        queue = deque()
        visit = set()

        # Add start to queue and visit
        queue.append((0, 0))
        visit.add((0, 0))


        # track length of paths
        length = 0
        # BFS
        while queue:
            # visit level
            for _ in range(len(queue)):
                # pop and grab next row and col
                r, c = queue.popleft()

                # destination case (return the shortest path)
                if r == rows - 1 and c == cols - 1:
                    return length

                # get directions
                direct = [[-1,0], [1,0], [0,-1], [0,1]]

                for dr, dc in direct:
                    # place holder for next path to check
                    row, col = r + dr, c + dc

                    # base case  same as dfs
                    if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 1 or (row, col) in visit:
                        continue    # next pair
                    
                    # add current vertex to queue and visit
                    queue.append((row, col))
                    visit.add((row, col))

            # update lenth 
            length += 1

        # return -1 
        return -1